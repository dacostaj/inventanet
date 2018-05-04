from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from almacenes.models import Categori, Product, Person, Entry, Stock
import json

# Create your views here.

def updateCategory(request):
		   name = request.POST.get('name')
		   description = request.POST.get('description')
		   id = request.POST.get('id')
		   

		   try:
		       category = Categori.objects.get(id=id)
		       category.name = name
		       category.description = description
		       category.save()
		       return HttpResponse(json.dumps({"mensaje": 'Categoria actualizada con exito','name': name, 'description': description}), content_type='application/json')
		   except:
		       return HttpResponse(json.dumps({"mensaje": "ERROR"}), content_type='application/json')

def updateProvider(request):
		   name = request.POST.get('name')
		   type_person = 'provider'
		   type_document = request.POST.get('type_document')
		   number_document = request.POST.get('number_document')
		   email = request.POST.get('email')
		   id = request.POST.get('id')
		   

		   try:
		       provider = Person.objects.get(id=id)
		       provider.name = name
		       provider.type_person = type_person
		       provider.type_document = type_document
		       provider.number_document = number_document
		       provider.email = email
		       provider.save()
		       return HttpResponse(json.dumps({"mensaje": 'Proveedor actualizado con exito','name': name, 'type_person': type_person, 'type_document': type_document, 'number_document': number_document, 'email': email}), content_type='application/json')
		   except:
		       return HttpResponse(json.dumps({"mensaje": "ERROR"}), content_type='application/json')


def deleteCategory(request):
		   id = request.GET.get('id')

		   try:
		       category = Categori.objects.get(id=id)
		       category.delete()
		       
		       return HttpResponse(json.dumps({"mensaje": 'Categoria Borrada con exito'}), content_type='application/json')
		   except:
		       return HttpResponse(json.dumps({"mensaje": "ERROR"}), content_type='application/json')

def deleteProduct(request):
		   id = request.GET.get('id')

		   try:
		       product = Product.objects.get(id=id)
		       product.delete()
		       
		       return HttpResponse(json.dumps({"mensaje": 'Producto Borrado con exito'}), content_type='application/json')
		   except:
		       return HttpResponse(json.dumps({"mensaje": "ERROR"}), content_type='application/json')

def deleteProvider(request):
		   id = request.GET.get('id')

		   try:
		       provider = Person.objects.get(id=id)
		       provider.delete()
		       
		       return HttpResponse(json.dumps({"mensaje": 'Proveedor Borrado con exito'}), content_type='application/json')
		   except:
		       return HttpResponse(json.dumps({"mensaje": "ERROR"}), content_type='application/json')


def insertCategory(request):
		   name = request.POST.get('name')
		   description = request.POST.get('description')

		   try:
		       category = Categori()
		       category.name = name
		       category.description = description
		       category.save()
		       return HttpResponse(json.dumps({"mensaje": 'Categoria Registrada con exito'}), content_type='application/json')
		   except:
		       return HttpResponse(json.dumps({"mensaje": "ERROR"}), content_type='application/json')

def insertProduct(request):
		   mark = request.POST.get('mark')
		   model = request.POST.get('model')
		   code = request.POST.get('code')
		   description = request.POST.get('description')
		   category = request.POST.get('categoryid')
		   image = 'media/default.png'

		   try:
		       product = Product()
		       product.mark = mark
		       product.model = model
		       product.code = code
		       product.description = description
		       product.categori_id = category
		       product.image = image
		       product.save()
		       return HttpResponse(json.dumps({"mensaje": 'Producto registrado con exito'}), content_type='application/json')
		   except:
		       return HttpResponse(json.dumps({"mensaje": "ERROR"}), content_type='application/json')

def insertProvider(request):
		   name = request.POST.get('name')
		   type_person = 'provider'
		   type_document = request.POST.get('type_document')
		   number_document = request.POST.get('number_document')
		   email = request.POST.get('email')

		   try:
		       provider = Person()
		       provider.name = name
		       provider.type_person = type_person
		       provider.type_document = type_document
		       provider.number_document = number_document
		       provider.email = email
		       provider.save()
		       return HttpResponse(json.dumps({"mensaje": 'Proveedor registrado con exito'}), content_type='application/json')
		   except:
		       return HttpResponse(json.dumps({"mensaje": "ERROR"}), content_type='application/json')


class HomeView(TemplateView):
	"""docstring for ClassName"""
	template_name = "almacenes/home.html"

class EntryView(TemplateView):
	"""docstring for ClassName"""
	template_name = "almacenes/entry/index.html"	

	def get_context_data(self, *args, **kwargs):
		entry = Entry.objects.all()
		product = Product.objects.all()
		provider = Person.objects.all()
		return {'entry': entry,'product': product,'provider': provider}
		

class ProviderView(TemplateView):
	"""docstring for ClassName"""
	template_name = "almacenes/provider/index.html"	

	def get_context_data(self, *args, **kwargs):
		provider = Person.objects.all()
		return {'provider': provider}


class CategoryView(TemplateView):
	"""docstring for ClassName"""
	template_name = "almacenes/category/index.html"	

	def get_context_data(self, *args, **kwargs):
		category = Categori.objects.all()
		return {'category':category}

class ProductView(TemplateView):
	"""docstring for ClassName"""
	template_name = "almacenes/product/index.html"	

	def get_context_data(self, *args, **kwargs):
		product = Product.objects.all()
		category = Categori.objects.all()
		return {'product':product, 'category': category}
		
    
	