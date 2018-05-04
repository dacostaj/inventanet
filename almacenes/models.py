from django.db import models

# Create your models here.
class Product(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	mark = models.CharField(max_length=255)
	model = models.CharField(max_length=255)
	code = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	image = models.ImageField()
	categori = models.ForeignKey(
		'almacenes.Categori', on_delete=models.CASCADE

		)
	def __str__(self):
		return self.description

class Categori(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	
	def __str__(self):
		return self.name

class Person(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	type_person = models.CharField(max_length=30)
	name = models.CharField(max_length=100)
	type_document = models.CharField(max_length=50)
	number_document = models.CharField(max_length=55)
	email = models.EmailField(max_length=100)
	def __str__(self):
		return self.name

class Entry(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	code_fact = models.CharField(max_length=100)
	person = models.ForeignKey(
		'almacenes.Person', on_delete=models.CASCADE

		)
	def __str__(self):
		return self.created_at

class Stock(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	plate = models.CharField(max_length=50)
	count = models.CharField(max_length=100)
	price_buy = models.FloatField()
	number_stock = models.IntegerField()
	serial = models.CharField(max_length=100)
	product = models.ForeignKey(
		'almacenes.Product', on_delete=models.CASCADE

		)
	entry = models.ForeignKey(
		'almacenes.Entry', on_delete=models.CASCADE

		)