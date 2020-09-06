from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',
                     'is_published', 'price',
                      'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor','state','city','price')
    list_editable = ('is_published',)
    search_fields = ('title','discription',
                     'address','city',
                     'state','zipcode',
                     'price','realtor__name')
    list_per_page = 12

admin.site.register(Listing,ListingAdmin)
