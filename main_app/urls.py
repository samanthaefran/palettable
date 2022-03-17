from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('products/<str:product_tag>/', views.products_index_by_tag, name='products_index'),
  path('product_detail/<int:id>/', views.products_detail, name='products_detail'),
  path('accounts/signup/', views.signup, name='signup'),
  path('favorites/', views.FavoriteList.as_view(), name='favorites_index'),
  path('products/<int:id>/add_favorite/', views.add_favorite, name='add_favorite'),
  path('products/<int:id>/delete_favorite/', views.delete_favorite, name='delete_favorite'),

    # path('products/<int:id>/add_favorite/', views.FavoriteCreate.as_view(), name='add_favorite'),

]