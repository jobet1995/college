from rest_framework import serializers
from .models import Parent, FinancialInformation


class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = '__all__'


class FinancialInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialInformation
        fields = '__all__'
