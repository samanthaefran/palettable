from django.shortcuts import render
from .models import Product, Color
from django.views.generic import ListView
# Create your views here.

class ProductIndex(ListView):
  model = Product