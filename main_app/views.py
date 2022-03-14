from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Color
# Create your views here.

def home(request):
  return HttpResponse('it works')

def about(request):
  return render(request, 'about.html')

def products(request):
  return render(request, 'products.html')

def products_index(request, product_type):
  products_list = Product.objects.filter(tags__contains=product_type)
  return render(request, 'products_index.html', {'products': products_list})

def product_detail(request, id):
  product = Product.objects.get(id=id)
  return render(request, 'product_detail.html', {'product': product})