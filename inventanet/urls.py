"""inventanet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import login, logout_then_login
from django.urls import path
from almacenes.views import (HomeView, CategoryView, insertCategory,
							 ProductView, deleteCategory, updateCategory,
							 insertProduct, deleteProduct, ProviderView,
                             insertProvider, updateProvider, deleteProvider,
                             EntryView )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',login,{'template_name': 'almacenes/login.html'},name='login'),
    path('logout/',logout_then_login,name='logout'),

    path('home/', HomeView.as_view(), name='home'),
    path('category', CategoryView.as_view(), name='category'),
    path('category/create', insertCategory, name='category-create'),
    path('category/delete', deleteCategory, name='category-delete'),
    path('category/update', updateCategory, name='category-update'),

    path('product', ProductView.as_view(), name='product'),
    path('product/create', insertProduct, name='product-create'),
    path('product/delete', deleteProduct, name='product-delete'),

    path('provider', ProviderView.as_view(), name='provider'),
    path('provider/create', insertProvider, name='provider-create'),
    path('provider/update', updateProvider, name='provider-update'),
    path('provider/delete', deleteProvider, name='provider-delete'),

    path('entry', EntryView.as_view(), name='entry'),
]
