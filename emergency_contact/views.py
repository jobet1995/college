from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models Emergency 
from .serializers import EmergencySerializer
from .forms import EmergencyForm
# Create your views here.
@api_view(['GET', 'POST'])
def emergency_list(request):
    if request.method == 'GET':
        data = Emergency.objects.all()
        serializer = EmergencySerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = EmergencySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['PUT', 'DELETE'])
def emergency_details(request, pk):
    try:
        emergency = Emergency.objects.get(pk=pk)
    except Emergency.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = EmergencySerializer(emergency, data=request.data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_500_BAD_REQUEST)
    elif request.method == 'DELETE':
        emergency.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)