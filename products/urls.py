from django.urls import path
from . import views

""" Product url paths """
urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>', views.product_detail, name='product_detail'),
]
