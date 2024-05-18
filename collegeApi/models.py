from django.db import models
from course.models import Course
from emergency_contact.models import Emergency
from parent.models import Parent
from instructor.models import Instructor
from enrollment.models import Enrollment
from subject.models import Subject
# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class collegeApi(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    emergency = models.ForeignKey(Emergency, on_delete=models.CASCADE)
    parent = models.Foreign(Parent, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    enrollment = models.Foreign(Enrollment, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
