from django import forms
from .models import Enrollment
from emergency_contact.models import Emergency
from parent.models import Parent
from course.models import Course


class EnrollmentForm(forms.ModelForm):
    course = forms.ModelChoiceField(queryset=Course.objects.all())
    parent = forms.ModelChoiceField(queryset=Parent.objects.all())
    emergency = forms.ModelChoiceField(
        queryset=Emergency.objects.all())

    class Meta:
        model = Enrollment
        fields = '__all__'
