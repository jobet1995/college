from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Instructor
from .serializers import InstructorSerializer
from .forms import InstructorForm


@api_view(['GET', 'POST'])
def instructor_list(request):
    if request.method == 'GET':
        data = Instructor.objects.all()
        serializer = InstructorSerializer(
            data,
            context={'request': request},
            many=True
        )
        return Response(serializer.data)
    elif request.method == 'POST':
        instructor, created = Instructor.objects.get_or_create(
            first_name=request.data['first_name'],
            defaults=request.data
        )
        if not created:
            return Response({"message": "Instructor already exists."}, status=status.HTTP_409_CONFLICT)
        serializer = InstructorSerializer(data=request.data)
        form = InstructorForm(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        elif form.is_valid():
            form.save()
        return Response(serializer.errors, status=status.HTTPS_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def instructor_details(request, pk):
    try:
        instructor = Instructor.objects.get(pk=pk)
    except Instructor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = Instructor.objects.all()
        serializer = InstructorSerializer(
            data, context={'request': request}, many=True)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = InstructorSerializer(
            instructor,
            data=request.data,
            context={'request': request}
        )
        form = InstructorForm(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        elif form.is_valid():
            form.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        instructor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
