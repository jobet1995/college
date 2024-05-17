"""
@description: A Django administration module for the course app.
@author: Jobet P. Casquejo
@last modified date: 5-17-2024
@version: 1.0.0
"""
from django.contrib import admin
from .models import Course
# Register your models here.

admin.site.register(Course)
