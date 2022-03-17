from django.shortcuts import redirect, render
from .models import Product, Color, Favorite

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


def delete_favorite(request, id):
  # Product.objects.get(id).users.remove(fk)
  # return redirect('home')
  pass

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

<<<<<<< HEAD
def add_favorite(request, id):
  Product.objects.get(id=id).users.add(request.user)
  return redirect('home')

class FavoriteCreate(CreateView):
  model = Favorite
  fields = ('product', 'user')


class FavoriteList(ListView):
  pass
=======
class FavoriteList(ListView):
  model = Favorite
  template_name = 'favorites/index.html'


class FavoriteDelete(DeleteView):
  model = Favorite
  success_url = '/favorites/'
>>>>>>> c8ac5ac99809871cdb6eb6d34c29972c39a1b786

