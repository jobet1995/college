from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import collegeApi
from .serializers import collegeApiSerializer
from django.http import HttpResponse


@api_view(['GET', 'POST'])
def college_list(request):
    if request.method == 'GET':
        data = collegeApi.objects.all()
        serializer = collegeApiSerializer(
            data, context={'request': request}, many=True
        )
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = collegeApiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTPS_500_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def college_details(request, pk):
    try:
        college = collegeApi.objects.get(pk=pk)
    except collegeApi.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = collegeApi.objects.all()
        serializer = collegeApiSerializer(
            data, context={'request': request}, many=True
        )
    elif request.method == 'PUT':
        serializer = collegeApiSerializer(
            college, data=request.data, context={'request': request}
        )

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_500_BAD_REQUEST)
    elif request.method == 'DELETE':
        college.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def index(request):
    data = collegeApi.objects.all()
    serializer = collegeApiSerializer(
        data, context={'request': request}, many=True)
    return Response(serializer.data)
