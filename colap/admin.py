from django.contrib import admin
from .models import Data

# Register your models here.
class DataAdmin(admin.ModelAdmin):
	list_display = ('data_collector','name','date_added','location','favourite_drink')
	list_filter =('data_collector','date_added','location','favourite_drink')
	search_fields=('location','favourite_drink')
	date_hierachy=('date_added')

admin.site.register(Data, DataAdmin)
