from django.shortcuts import render,get_object_or_404, redirect
from django.views import generic
from .models import Product
from order.models import Order, OrderProduct
from django.contrib import messages

class HomeListView(generic.ListView):
	template_name = 'products/home.html'
	model = Product
	context_object_name = 'products'

class ProductDetailView(generic.DetailView):
	template_name = 'products/product-detail.html'
	model = Product
	context_object_name = 'product'

def add_to_cart(request, slug):
	product = get_object_or_404(Product, slug=slug)
	order, created= Order.objects.get_or_create(user = request.user)
	queryset = OrderProduct.objects.filter(order= order,
												 product= product, carted= True)
	if queryset.exists():
		messages.info(request, "This product already in your Cart !!")
		return redirect('/')
	else:
		OrderProduct.objects.create(order = order,
										product= product, carted= True)
		messages.info(request, "Product is successfull added your Cart !!")
		return redirect('/')

def remove_from_cart(request, slug):
	product = get_object_or_404(Product, slug=slug)
	order, created= Order.objects.get_or_create(user = request.user)
	queryset = OrderProduct.objects.filter(order= order,
												 product= product, carted= True)
	if queryset.exists():

		query = queryset[0]
		query.delete()
		messages.info(request, "The product is removed !!")
		return redirect('products:product_detail', slug=slug)
	return redirect('/')

def remove_single_product_from_cart(request, slug):
	product = get_object_or_404(Product, slug= slug)
	queryset = OrderProduct.objects.filter(product = product, order__user=request.user, carted= True)
	if queryset.exists():
		q = queryset[0]
		if q.quantity > 1 :
			q.quantity -= 1
			q.save()
			messages.info(request, "The product quantity updated !!")
		else :
			q.delete()
			messages.info(request, "The product is removed !!")
	else:
		messages.info(request, "This Product is not your cart !!")
	return redirect('order:cart_view')

def add_single_product_to_cart(request, slug):
	product = get_object_or_404(Product, slug= slug)
	queryset = OrderProduct.objects.filter(product = product, order__user=request.user, carted= True)
	if queryset.exists():
		query = queryset[0]
		query.quantity +=1
		query.save()
		messages.info(request, "The product quantity is updates!!")
	else:

		messages.info(request, "This Product is not your cart !!")
	return redirect('order:cart_view')
		


	

















