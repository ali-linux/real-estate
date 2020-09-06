from django.shortcuts import render
from listings.choices import price_choices,bedroom_choices,state_choices
from listings.models import Listing
from realtors.models import Realtor
def index(request):
    listings = Listing.objects.order_by('-list_date')

    context = {
        'listings':listings,
        'state_choices':state_choices,
        'bedroom_choices':bedroom_choices,
        'price_choices':price_choices,
        }
    return render(request,'pages/index.html',context)

def about(request):
    realtors = Realtor.objects.all()
    mvp = Realtor.objects.all().filter(realtor_of_month=True)[:1]
    context = {
        'realtors':realtors,
        'mvp':mvp
        }
    return render(request , 'pages/about.html',context)
