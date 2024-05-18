from django import forms
from .models import collegeApi
from course.models import Course
from emergency_contact.models import Emergency
from parent.models import Parent
from instructor.models import Instructor
from enrollment.models import Enrollment
from subject.models import Subject


class collegeApiForms(forms.ModelForm):
    course = forms.ModelChoiceField(queryset=Course.objects.all())
    parent = forms.ModelChoiceField(queryset=Parent.objects.all())
    emergency = forms.ModelChoiceField(
        queryset=Emergency.objects.all())
    instructor = forms.ModelChoiceField(queryset=Instructor.objects.all())
    enrollment = forms.ModelChoiceField(queryset=Enrollment.objects.all())
    subject = forms.ModelChoiceField(queryset=Subject.objects.all())

    class Meta:
        model = collegeApi
        fields = '__all__'
