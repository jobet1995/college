from django.db import models
from course.models import Course
from emergency_contact.models import Emergency


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Enrollment(BaseModel):
    gender = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('N/A', 'N/A'),
    )
    application_type = [
        ('Freshman', 'Freshman'),
        ('Transferee', 'Transferee'),
        ('Other', 'Other')
    ]
    admission_application = [
        ('1st Semester', '1st Semester'),
        ('2nd Semester', '2nd Semester'),
        ('Summer', 'Summer')
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=3, choices=gender)
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=10)
    application_type = models.CharField(
        max_length=255, choices=application_type)
    admission_application = models.CharField(
        max_length=255, choices=admission_application)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name_of_last_high_school_attended = models.CharField(max_length=255)
    year_graduated = models.DateField()
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=10)
    ranking_in_graduation_class = models.CharField(max_length=255)
    lastest_gwa_percentile = models.CharField(max_length=255)
    recognition = models.TextField(max_length=255)
    high_school_organization = models.TextField(max_length=255)
    Name_of_College_Last_Attended = models.TextField(max_length=255)
    course_taken = models.TextField(max_length=255)
    academic_year_last_attended = models.TextField(max_length=255)
    college_achievement = models.TextField(max_length=255)
    emergency = models.ForeignKey(Emergency, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
