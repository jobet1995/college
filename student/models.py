from django.db import models
from enrollment import Enrollment
# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Student(BaseModel):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    date_signed_by_applicant = models.DateField()
    applicant_signature = models.CharField(max_length=100)

    def __str__(self):
        return self.enrollment
