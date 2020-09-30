from django.urls import path
from .views import (HomeListView, ProductDetailView, 
					add_to_cart, remove_from_cart,
					remove_single_product_from_cart,
					add_single_product_to_cart
					
					)
app_name = 'products'
urlpatterns = [

	path('', HomeListView.as_view(), name= 'home'),
	path('detail/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
   	path('add-to-cart/<slug:slug>/', add_to_cart, name= 'add-to-cart'),
   	path('remove-from-cart/<slug:slug>/', remove_from_cart, name= 'remove-from-cart'),
	path('remove-single-product-from-cart/<slug:slug>/', remove_single_product_from_cart, name= 'remove-single'),
	path('add-single-product-to-cart/<slug:slug>/', add_single_product_to_cart, name= 'add-single')

]