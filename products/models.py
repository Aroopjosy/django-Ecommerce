from django.db import models
from django.db.models.signals import pre_save
from ecommerce.utils import unique_slug_generator
from django.urls import reverse


PRODUCT_AVAILABILITY = (
			('OUT', "Out of Stok"),
			('IN', 'In Stock')
	)

 

class Product(models.Model):
	title = models.CharField(max_length=200)
	price = models.FloatField(blank=True, null=True)
	discount_price = models.FloatField(blank=True, null=True)
	description = models.TextField(blank=True, null=True)
	image = models.ImageField(upload_to='product-img/',blank=True, null=True)
	available = models.CharField(max_length=3, choices=PRODUCT_AVAILABILITY,blank=True, null=True)
	slug = models.SlugField(blank=True, null=True)

	def __str__(self):

		return self.title

	def get_absolute_url(self):
		return reverse('products:product_detail', kwargs= {'slug':self.slug})

def slug_generator(sender, instance, *args, **kwargs):

	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator, sender=Product)

