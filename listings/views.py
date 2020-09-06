from django.shortcuts import render, get_object_or_404
from .models import Listing
from realtors.models import Realtor
from .choices import state_choices,price_choices,bedroom_choices
from django.core.paginator import Paginator, PageNotAnInteger,EmptyPage

def listings(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings,6)
    page = request.GET.get('page')
    paged_listing = paginator.get_page(page)

    context = {"listings":paged_listing}
    return render(request, 'listings/listings.html',context)

def listing(request,listing_id,title):
    #listing = Listing.objects.get(id=listing_id)
    listing = get_object_or_404(Listing, pk = listing_id)
    realtor = Realtor.objects.get(name = listing.realtor)
    context = {"listing":listing,"realtor":realtor}

    return render(request, 'listings/listing.html', context)

def search(request):
    listings_query = Listing.objects.order_by('-list_date').filter(is_published=True)

    #keywords
    if 'words' in request.GET:
        keyword = request.GET['words']
        if keyword:
            listings_query = listings_query.filter(discription__icontains = keyword)

    #City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            listings_query = listings_query.filter(city__iexact = city)

    #State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            listings_query = listings_query.filter(state__iexact = state)

    #price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            listings_query = listings_query.filter(price__lte = price)

    #bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            listings_query = listings_query.filter(bedrooms__lte = bedrooms)

    context = {

        'state_choices':state_choices,
        'bedroom_choices':bedroom_choices,
        'price_choices':price_choices,
        'listings':listings_query,
        'values':request.GET,

    }
    return render(request, 'listings/search.html', context)
