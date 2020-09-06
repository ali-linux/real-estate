from django.contrib import admin
from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id','name','phone','email',
                    'realtor_of_month','hire_date')
    list_display_links = ('id','name')
    #list_filter = ('name','hire_date')
    list_editable = ('realtor_of_month',)
    search_fields = ('name','phone','email')

    list_per_page = 12

admin.site.register(Realtor,RealtorAdmin)

