from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('products/<str:product_tag>/', views.products_index_by_tag, name='products_index'),
  path('product_detail/<int:id>/', views.products_detail, name='products_detail'),
  path('accounts/signup/', views.signup, name='signup'),
]