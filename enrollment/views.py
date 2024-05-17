from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Enrollment
from .serializers import EnrollmentSerializer


@api_view(['GET', 'POST'])
def enrollment_list(request):
    if request.method == 'GET':
        data = Enrollment.objects.all()
        serializer = EnrollmentSerializer(
            data, context={'request': request}, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EnrollmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
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
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        enrollment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
