from django import forms
from .models import Parent, FinancialInformation


class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = '__all__'


class FinancialInformationForm(forms.ModelForm):
    class Meta:
        model = FinancialInformation
        fields = '__all__'
