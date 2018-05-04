from django.contrib import admin
from almacenes.models import Categori, Product, Person, Entry, Stock

# Register your models here.



class CategoriAdmin(admin.ModelAdmin): 
	list_display = ('name', 'description') 

class ProductAdmin(admin.ModelAdmin): 
	list_display = ('mark','model','code','description','image','categori') 

class PersonAdmin(admin.ModelAdmin): 
	list_display = ('type_person','name','type_document','number_document','email') 

class EntryAdmin(admin.ModelAdmin): 
	list_display = ('created_at','code_fact','person') 

class StockAdmin(admin.ModelAdmin): 
	list_display = ('plate','count','price_buy','number_stock','serial','product') 

admin.site.register(Categori, CategoriAdmin)
admin.site.register(Product, ProductAdmin) 
admin.site.register(Person, PersonAdmin)
admin.site.register(Entry, EntryAdmin)
admin.site.register(Stock, StockAdmin) 