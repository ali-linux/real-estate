from django.shortcuts import render,redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail
def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']
        title = request.POST['title']

        #CHECK IF USER HAS MADE INQUIRY ALREADY
        if request.user.is_authenticated:
            user_id = request.user.id
            has_connected = Contact.objects.filter(listing_id=listing_id, user_id=user_id).exists()
            if has_connected:
                messages.error(request,'Already submitted an inquiry')
                return redirect('/listings/'+listing_id+'/'+title)

        contact = Contact(listing = listing, listing_id= listing_id,
            name=name, email=email, phone=phone,
            message=message, user_id=user_id)

        contact.save()

        #SEND EMAIL TO REALTOR
        send_mail(
            'Property Listing ',
            'there has been a inquiry for ' + '. Sign into the admin panel for more info',
            'ali.srwsht.ali@gmail.com',
            [realtor_email],
            fail_silently=False
            )

        messages.success(request,'your request has been submitted, we will get back to you as soon as possible')
    return redirect('/listings/'+listing_id+'/'+title)

