from django.shortcuts import redirect, render
from .models import Product, Color

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView

# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def products_index_by_tag(request, product_tag):
  if product_tag == 'Vegan':
      products_list = Product.objects.filter(tags__icontains=product_tag)
  elif product_tag == 'cruelty-free' or product_tag == 'cruelty free':
      sanitized_product_tag = product_tag.replace('-', ' ')
      products_list = Product.objects.filter(tags__icontains=sanitized_product_tag)
  elif product_tag == 'natural':
      products_list = Product.objects.filter(tags__icontains=product_tag)
  else: 
    return redirect('home')
  return render(request, 'products_index.html', {'product': products_list})

def products_detail(request, id):
  product = Product.objects.get(id=id)
  # colors = Color.objects.filter(product=id)
  return render(request, 'products/detail.html', {'product': product})
  # colors = Color.objects.filter(product=id) - right now we are not pulling color somehow? it breaks the file as of now.

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid Sign Up - Please Try Again'
  form = UserCreationForm()
  context = { 'form': form, 'error': error_message }
  return render(request, 'registration/signup.html', {'form': form, 'error': error_message})

def favorite_add(request, id, user_id):
  Product.objects.get(id=id).favorites.add(request.user)
  return redirect('home')

def favorite_remove(request, id, user_id):
  Product.objects.get(id=id).favorites.remove(request.user)
  return redirect('home')

def favorite_list(request, user_id):
  favorites = Product.objects.filter(favorites=request.user)
  return render(request, 'favorites/index.html', {'favorites': favorites})




