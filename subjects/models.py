from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Subject(BaseModel):
    subject_name = models.CharField(max_length=255)
    subject_code = models.CharField(max_length=255)
    schedule = models.CharField(max_length=255)
