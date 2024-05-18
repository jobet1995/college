from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Parent, FinancialInformation
from .serializer import ParentSerializer, FinancialInformationSerializer

@api_view(['GET', 'POST'])
def parent_list(request):
  if request.method == 'GET':
    data = Parent.objects.all()
    serializer = ParentSerializer(data, context={'request': request}, many=True)
    return Response(serializer.data)
  elif request.method == 'POST':
    serializer = ParentSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)