from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('products/<str:product_tag>/', views.products_index_by_tag, name='products_index'),
  path('product_detail/<int:id>/', views.products_detail, name='products_detail'),
  path('accounts/signup/', views.signup, name='signup'),

  # path('favorites/', views.FavoriteList.as_view(), name='favorites_index'),
  # path('favorites/<int:id>/delete', views.FavoriteDelete.as_view(), name='favorites_delete'),
