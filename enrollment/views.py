from django.shortcuts import render
from rest_framework.response import Response, IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import APIVIEW
from .models import Enrollment
from .serializers import EnrollmentSerializer
from .forms import EnrollmentForm


@api_view(['GET', 'POST'])
def enrollment_list(request):
    if request.method == 'GET':
        data = Enrollment.objects.all()
        serializer = EnrollmentSerializer(
            data, context={'request': request}, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EnrollmentSerializer(data=request.data)
        form = EnrollmentForm(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        elif form.is_valid():
            form.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTPS_500_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def enrollment_details(request, pk):
    try:
        enrollment = Enrollment.objects.get(pk=pk)
    except Enrollment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = EnrollmentSerializer(
            enrollment, data=request.data, context={'request': request})
        form = EnrollmentForm(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        elif form.is_valid():
            form.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        enrollment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EnrollmentInfo(APIVIEW):
    permission_classes = (IsAuthenticated)

    def get(self, request, enrollment_form, enrollment_id):
        try:
            Enrollment.objects.create_enrollment(
                enrollment_form, enrollment_id)
            return Response({
                "Status": "A new Enrollment Added",
            }, status=status.HTTP_200_OK)
        except Exception as err:
            return Response({
                "Status": "An Record Existed"
            }, status=status.HTTP_400_BAD_REQUEST)


class CreateEnrollment(APIVIEW):
    permission_classes = (IsAuthenticated)

    def post(self, request):
        create_enrollment_serializer = EnrollmentSerializer(data=request.data)
        if create_enrollment_serializer.is_valid():
            create_enrollment_serializer.save()
            return Response({"Status": "Success"}, status=status.HTTP_200_OK)
        else:
            return Response({"Status": create_student_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
