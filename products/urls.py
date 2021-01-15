from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('products_criteria/', views.products_criteria, name='products_criteria'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
]
