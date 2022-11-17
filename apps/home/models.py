# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PostuladorPaseo(models.Model):
	nombres=models.CharField(max_length=30)
	apellidos=models.CharField(max_length=30)
	correo=models.CharField(max_length=30)
	nacimiento = models.DateField()
	mensaje=models.CharField(max_length=1000)
	cv=models.FileField()
	def __str__(self):
		return self.nombres