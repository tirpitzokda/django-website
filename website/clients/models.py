from django.db import models
from django.contrib.auth.models import User, Group, Permission
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType



class Product(models.Model):
	name = models.CharField(max_length=100)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	quantity = models.PositiveIntegerField()
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name