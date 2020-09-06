from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from contacts.models import Contact
from django.core.mail import send_mail
from .models import password_reset
import secrets
from datetime import datetime
from django.utils import timezone
def login(request):
    #CHECK IF THE SUBIMTED FORM IS A POST REQUEST NOT A GET REQUEST
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        #STORE SUBMITED DATA INTO VARIBELS
        username = request.POST['username-email']
        email = request.POST['username-email']
        password = request.POST['password']
        #CHECK IF USER CREDENTIALS VALID
        user_name = auth.authenticate(request, username=username, password=password)
        user_email_check = User.objects.filter(email=email).exists()
        if user_email_check:
            user_valid = User.objects.get(email=email)
            user_1 = auth.authenticate(request, username = user_valid.username, password = password)
            if user_1 is not None:
                auth.login(request,user_1)
                messages.success(request,'logged in successfully')
                return redirect('dashboard')
            else:
                messages.error(request,'inavlid credentials')
                return redirect('login')
        if user_name  is not None :
            auth.login(request,user_name)
            messages.success(request,'logged in successfully')
            return redirect('dashboard')

        else:
            messages.error(request,'inavlid credentials')
            return redirect('login')
    return render(request,'accounts/login.html')


def register(request):
    #CHECK IF THE SUBIMTED FORM IS A POST REQUEST NOT A GET REQUEST
    if request.method == 'POST':
        #STORE SUBMITED DATA INTO VARIBELS
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        #CHECK IF THE PASSWORDS MATCH
        if password != password2:
            messages.error(request,'passwords dont match')
            return redirect('register')
        else:
            #check for duplicate usernames
            user_name = User.objects.filter(username=username).exists()
            if user_name:
                messages.error(request,'username already taken')
                return redirect('register')

            else:
                #check for duplicate emails
                user_email = User.objects.filter(email=email).exists()
                if user_email:
                    messages.error(request,'email already taken')
                    return redirect('register')
                else:
                    #EVERYTHING IS VALID
                    user = User.objects.create_user(username=username,email=email, password=password)
                    user.save()
                    messages.success(request,'gooooooooooood!')
                    return redirect('login')

    else:
        return render(request,'accounts/register.html')




def password_reset_func(request):
    if request.method == 'POST':
        user_email = request.POST['email']
        user_email_exst = User.objects.filter(email=user_email).exists()
        if user_email_exst:
            user_token = secrets.token_urlsafe(16)
            send_mail('Password Reset','https://nwsinga.herokuapp.com/accounts/password/reset/done/{}'.format(user_token),
            'ali.srwsht.ali@gmail.com',[user_email],fail_silently=False)
            messages.success(request,'shortly you will recive an email with instructions to reset your password do not share that link with any one')
            reset = password_reset(user_email=user_email,user_token=user_token)
            reset.save()
        else:
            messages.error(request,"there is no user with that email")
            return redirect('password_reset')
    return render(request,'accounts/reset_password.html')

def time_t (obejt_str):
    date_ = obejt_str.split('-',2)
    #date_[0] == year, date_[1] == month
    date_day = date_[2].split() #date_day[0] == the day
    time_ = obejt_str.split(':')
    time_hour = time_[0].split()
    day = int(date_day[0])
    month = int(date_[1])
    year = int( date_[0])
    hour = int(time_hour[1])
    minute = int(time_[1])
    context = {'date':obejt_str,
                'day':day,'month':month,'year':year,
                'hour':hour, 'minute':minute, 'date':obejt_str
                }
    return context

def password_reset_done(request,token):
    user_token_rest = password_reset.objects.filter(user_token=token).exists()
    if user_token_rest:
        request_date = password_reset.objects.get(user_token=token)
        time_request = time_t(str(request_date.date_request))
        time_now = time_t(str(timezone.now()))
        #datetime_object = datetime.strptime(request_date.date_request, "%d-%b-%Y  %H:%M:%S.%f")
        if time_request['day'] == time_now['day'] and time_request['month'] == time_now['month'] and time_request['year'] == time_now['year']:
            if time_request['hour'] == time_now['hour']:
                x = time_now['minute']-time_request['minute']
                if x < 5:
                    if request.method == 'POST':
                            password = request.POST['password1']
                            password2 = request.POST['password2']
                            if password != password2:
                                messages.error(request,'passwords dont match')
                                return redirect('password_reset_done',token)
                            else:
                                user_info = password_reset.objects.get(user_token=token)
                                user_reset = User.objects.get(email=user_info.user_email)
                                user_reset.set_password(password)
                                user_reset.save()
                                messages.success(request,'password successfuly updated')
                                password_reset.objects.filter(user_token=token).delete()
                                return redirect('login')
                else:
                    password_reset.objects.filter(user_token=token).delete()
                    messages.error(request,'time expierd make a new request')
                    return redirect('password_reset')
    else:
        messages.error(request,'invalid Token')
        return redirect('index')
    context = {'token':token}
    return render(request,'accounts/password_reset_done.html', context)
    # token = str(tokenn)
    # print(token)
    # print(user_token_rest)
    # if request.method == 'POST':
    #     if user_token_rest:
    #         return redirect('about')
    #     if user_token_rest:
    #         print('heloooooooooooooooooooooooooooo')
@login_required
def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('index')
    else:
        user1 = request.user.id
        user_info = Contact.objects.filter(user_id=user1)

        context = {'info': user_info}
        return render(request, 'accounts/dashboard.html', context)

@login_required
def logout(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            auth.logout(request)
            return redirect('index')
        else:
            return redirect('dashboard')
    else:
        return redirect('index')
