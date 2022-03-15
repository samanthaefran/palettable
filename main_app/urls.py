from django.urls import path
from . import views

urlpatterns = [
  path('', views.ProductIndex.as_view(template_name='product_list.html'), name='product_index'),
]