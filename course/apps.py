"""
@description: A Django administration module for the course app.
@author: Jobet P. Casquejo
@last modified date: 5-17-2024
@version: 1.0.0
"""
from django.apps import AppConfig


class CourseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'course'
