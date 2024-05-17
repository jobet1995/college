from rest_framework import serializers
from .models import Enrollment
from emergency_contact.models import Emergency
from parent.models import Parent
from course.models import Course

class EnrollmentSerializer(serializers.ModelSerializer):
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())
    parent = serializers.PrimaryKeyRelatedField(queryset=Parent.objects.all())
    emergency = serializers.PrimaryKeyRelatedField(
        queryset=Emergency.objects.all())

    class Meta:
        model = Enrollment
        fields = '__all__'
