from django.shortcuts import render, redirect, get_object_or_404
from .models import Order, OrderProduct, Address
from products.models import Product
from django.views import View
from django.contrib import messages
from django.conf import settings
from .forms import CheckoutForm
import stripe 

# Set your secret key. Remember to switch to your live secret key in production!
# See your keys here: https://dashboard.stripe.com/account/apikeys
stripe.api_key ='sk_test_51HDpedCBNEm08gJKYfP5vpzCx2BkdYTx7F4uQyLdp4z0j3dvfgSN0eDHA1zESGpQDqSVEGfA9fDgj09CuATgCk1E00GLSPxayu'




def cart_view(request):
	try:
		order = Order.objects.filter(user = request.user)[0]
		queryset = order.orderproduct_set.filter(carted= True)
		# p = Product.objects.filter(orderproduct__in= queryset)
		context = {
			'cart':queryset,
			'object':order
		}
		return render(request, 'order/cart.html',context )
	except:
		 messages.warning(request, "you don't have an active order")
		 return redirect('products:home')

	

class ChechoutProcess(View):
	
	def get(self, *args, **kwargs):
		try:
			order = Order.objects.get(user= self.request.user)
			print(order)
			products = order.orderproduct_set.filter(carted= True)
			print(products)
			context={
					'form': CheckoutForm(),
					'order': order,
					'products': products
				}
			return render(self.request, 'checkout.html', context)
		except:
			messages.warning(self.request, "You dont have no active orders")
			return redirect('order:cart_view')

	def post(self, *args, **kwargs):
		form = CheckoutForm(self.request.POST)
		try:
			order = Order.objects.get(user= self.request.user)
			if form.is_valid():
				user = self.request.user
				street_address = form.cleaned_data.get('street_address')
				apartment_address = form.cleaned_data.get('apartment_address')
				country = form.cleaned_data.get('country')
				zip_code = form.cleaned_data.get('zip_code')

				address = Address(
					user = user,
					street_address = street_address,
					apartment_address = apartment_address,
					country = country,
					zip_code = zip_code
				)
				address.save()
				order.address =address
				print(order)
				print('before')
				order.save()
				print('after')
				messages.info(self.request, "you checkout process completed")

				return redirect('order:stripe')
		except:
			messages.info(self.request, "checkout process Failed")
			return redirect('order:cart_view')

class PaymentView(View):

	def get(self, *args, **kwargs):
		order = Order.objects.filter(user = self.request.user)
		context = {
			'order':order
		}

		return render(self.request, 'order/stripe_payment.html', context)
	
	def post(self, *args, **kwargs):
		# Set your secret key. Remember to switch to your live secret key in production!
		# See your keys here: https://dashboard.stripe.com/account/apikeys

		# Token is created using Stripe Checkout or Elements!
		# Get the payment token ID submitted by the form:
		try:

			token = self.request.POST['stripeToken']
			print(token)
			customer = stripe.Customer.create(
				name = self.request.user.username,
				email = self.request.user.email,
				source = token
			)
			order = Order.objects.filter(user = self.request.user)[0]
			orderproduct = order.orderproduct_set.filter(carted= True)
			
			amount = int(order.get_total() * 100)
			print(token)
			stripe.Charge.create(
			customer = customer,
			amount=amount,
			currency='inr',
			description='ecommerce',
			# source = token
			)
			# for product in orderproduct:
			# 	product.ordered = True
			# 	product.carted = False
			# 	product.save()
			orderproduct.update(ordered = True, carted= False)

			messages.info(self.request, "transaction completed!!")
			return redirect('/')
		except Exception as e:
			messages.info(self.request, f"payment incomplete{e}")
			return redirect('/')

		
		

	

