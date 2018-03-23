from django.db import models
from django.utils import timezone

# Create your models here.
###############################################################################
class ContactMessage(models.Model):
	'''
		If a customer wants to message the shop.
	'''
	class Meta:
		verbose_name = 'Message privé'
		verbose_name_plural = 'Message privés'
	# Attributes
	uid = models.AutoField(
		primary_key= True, db_index= True)
	nom = models.CharField(
		max_length = 100)
	contenu = models.TextField(
		)
	remote_addr = models.CharField(
		max_length = 400)
	timestamp = models.DateTimeField(
		default = timezone.now)
	# Methods
	def __str__(self):
		return str(self.uid)