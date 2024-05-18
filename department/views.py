from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Department
from .serializers import DepartmentSerializers
# Create your views here.


@api_view(['GET', 'POST'])
def department_list(request):
    if request.method == 'GET':
        data = Department.objects.all()
        serializer = DepartmentSerializers(
            data,
            context={'request': request},
            many=True
        )
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DepartmentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def department_details(request, pk):
    try:
        department = Department.objects.get(pk=pk)
    except Department.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DepartmentSerializers(
            department, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DepartmentSerializers(
            department,
            data=request.data,
            context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        department.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)