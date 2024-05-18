from rest_framework import serializers
from .models import Instructor
from department.models import Department


class InstructorSerializer(serializers.ModelSerializer):
    department = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all())

    class Meta:
        model = Instructor
        fields = '__all__'
