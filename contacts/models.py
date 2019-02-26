from django.db import models
from datetime import datetime
from pytz import timezone

class Contact(models.Model):
	name_last=models.CharField(max_length=50,default='')
	name_first=models.CharField(max_length=50,default='')
	email=models.EmailField(max_length=70,default='')
	phone=models.CharField(max_length=12,default='')
	address_st1=models.CharField(max_length=50,default='')
	address_st2=models.CharField(max_length=50,default='',blank=True)
	address_city=models.CharField(max_length=50,default='')
	address_state=models.CharField(max_length=20,default='')
	address_zip=models.CharField(max_length=5,default='')
	comments=models.TextField(default='',blank=True)
	date_submitted=models.DateTimeField(default=datetime.now(timezone('America/Chicago')))
	status=models.CharField(max_length=50,default='')

	def __str__(self):
		return '_'.join([self.name_last,self.name_first,self.address_st1])



class Unsubscribe(models.Model):
	address_st1=models.CharField(max_length=50,default='')
	address_st2=models.CharField(max_length=50,default='',blank=True)
	address_city=models.CharField(max_length=50,default='')
	address_state=models.CharField(max_length=20,default='')
	address_zip=models.CharField(max_length=5,default='')
	
	def __str__(self):
		return '_'.join([self.address_st1,self.address_city])