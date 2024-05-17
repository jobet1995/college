"""
@description: A Django administration module for the course app.
@author: Jobet P. Casquejo
@last modified date: 5-17-2024
@version: 1.0.0
"""
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Course(BaseModel):
    course_name = models.CharField(max_length=255)
    course_description = models.TextField(max_length=255)

    def __str__(self):
        return self.course_name
