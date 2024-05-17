from django import forms
from .models.emergency import Emergency

class EmergencyForm(forms.ModelForm):
    class Meta:
        model = Emergency
        fields = '__all__'