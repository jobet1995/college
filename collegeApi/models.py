from django.db import models
from course.models import Course
from emergency_contact.models import Emergency
from parent.models import Parent
# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class collegeApi(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    emergency = models.ForeignKey(Emergency, on_delete=models.CASCADE)
