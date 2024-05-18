from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Parent, FinancialInformation
from .serializer import ParentSerializer, FinancialInformationSerializer
from .forms import ParentForm, FinancialInformationForm


@api_view(['GET', 'POST'])
def parent_list(request):
    if request.method == 'GET':
        data = Parent.objects.all()
        serializer = ParentSerializer(
            data, context={'request': request}, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ParentSerializer(data=request.data)
        form = ParentForm(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        elif form.is_valid():
            form.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def parent_details(request, pk):
    try:
        parent = Parent.objects.get(pk=pk)
    except Parent.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ParentSerializer(parent, context={'request': request})
        return Response(serializer.create)
    elif request.method == 'PUT':
        serializer = ParentSerializer(
            parent, data=request.data, context={'request': request})
        form = ParentForm(parent, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        elif form.is_valid():
            form.is_valid()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        parent.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def financial_list(request):
    if request.method == 'GET':
        data = FinancialInformation.objects.all()
        serializer = FinancialInformationSerializer(
            data, context={'request': request},
            many=True
        )
        return Response(serializer.create)
    elif request.method == 'POST':
        serializer = FinancialInformationSerializer(data=request.data)
        form = FinancialInformationForm(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        elif form.is_valid():
            form.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def financial_list(request, pk):
    if request.method == 'GET':
        data = FinancialInformation.objects.all()
        serializer = FinancialInformationSerializer(
            data, context={'request': request},
            many=True
        )
        return Response(serializer.create)
    elif request.method == 'POST':
        serializer = FinancialInformationSerializer(data=request.data)
        form = FinancialInformationForm(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        elif form.is_valid():
            form.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def financial_details(request, pk):
    try:
        financial = FinancialInformation.objects.get(pk=pk)
    except FinancialInformation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = FinancialInformationSerializer(
            financial, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = FinancialInformationSerializer(
            financial,
            data=request.data,
            context={'request': request}
        )
        form = FinancialInformationForm(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        elif form.is_valid():
            form.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        financial.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
