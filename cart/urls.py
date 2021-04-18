from django.urls import path
from . import views, contexts

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add/<item_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('modify/<item_id>/', views.mod_cart, name='mod_cart'),
    path('cart_contents/', contexts.cart_contents, name='cart_contents'),
]
