from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('products/', views.products, name='products'),
  path('products/<str:product_type>/', views.products_index, name='product_index'),
  path('product_detail/<int:id>/', views.products_detail, name='products_detail'),
]