from django.db import models
from department.models import Department
# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Instructor(BaseModel):
    gender = [
        ('Male', 'male'),
        ('Female', 'female'),
        ('Other', 'other')
    ]
    first_name = models.CharField(max_length=255, null=False)
    middle_initial = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=False)
    gender = models.CharField(choices=gender, max_length=255)
    birtdate = models.DateField()
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
