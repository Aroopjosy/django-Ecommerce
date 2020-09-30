# from django.db.models.signals import pre_save
# from django.dispath import recevier
# from .models import Product
# from django.utils.text import slugify


# def slugstring(instance):
# 	string = instance.title
# 	slug = slugify(string)
# 	return slug
# @recevier(pre_save, sender = Product)
# def pre_save_slug(sender, instance, *args, **kwargs):

# 	instance.slug = slugify(instance.title )




