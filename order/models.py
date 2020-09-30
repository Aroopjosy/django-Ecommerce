from django.db import models
from django.conf import settings
from products.models import Product
from django.utils import timezone
from django_countries.fields import CountryField



class Order(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	carted_date = models.DateTimeField(null=True, blank= True)
	ordered_date = models.DateTimeField(null=True, blank= True)
	address = models.ForeignKey('Address', on_delete= models.SET_NULL, null= True, blank=True)
	def __str__(self):
		return self.user.username
	def get_total(self):
		tottal= 0
		for order_product in self.orderproduct_set.filter(carted= True):
			tottal += order_product.get_final_price()
		return tottal


class OrderProduct(models.Model):
	order = models.ForeignKey(Order, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity = models.IntegerField(default=1)
	ordered = models.BooleanField(default=False)
	carted = models.BooleanField(default=False)
	
	

	def __str__(self):
		return f"{self.quantity} of {self.product.title}"

	def get_total_product_price(self):
		return self.product.price * self.quantity
	
	def get_total_product_discount_price(self):
		return self.product.discount_price * self.quantity

	def get_final_price(self):
		if self.product.discount_price :
			return self.get_total_product_discount_price()
		return self.get_total_product_price()

class Address(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	apartment_address = models.CharField(max_length=200)
	street_address = models.CharField(max_length=200)
	country = CountryField(multiple= False)
	zip_code = models.CharField(max_length=10)

	def __str__(self):
		return "%s of %s" %(self.user.username, self.street_address)





	



	


