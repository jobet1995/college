from rest_framework import serializers
from .models import collegeApi
from course.models import Course
from emergency_contact.models import Emergency
from parent.models import Parent
from instructor.models import Instructor
from enrollment.models import Enrollment
from subject.models import Subject


class collegeApiSerializer(serializers.ModelSerializer):
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())
    emergency_contact = serializers.PrimaryKeyRelatedField(
        queryset=Emergency.objects.all())
    parent = serializers.PrimaryKeyRelatedField(queryset=Parent.objects.all())
    instructor = serializers.PrimaryKeyRelatedField(
        queryset=Instructor.objects.all())
    enrollment = serializers.PrimaryKeyRelatedField(
        queryset=Enrollment.objects.all())
    subject = serializers.PrimaryKeyRelatedField(
        queryset=Subject.objects.all())

    class Meta:
        model = collegeApi
        fields = '__all__'
