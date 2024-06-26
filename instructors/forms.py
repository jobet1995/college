from django import forms
from .models import Instructor
from department.models import Department


class InstructorForm(forms.ModelForm):
    department = forms.ModelChoiceField(queryset=Department.objects.all())

    class Meta:
        model = Instructor
        fields = '__all__'
