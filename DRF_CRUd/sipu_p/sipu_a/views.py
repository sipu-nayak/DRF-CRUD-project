from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CompanyDetails
from .serializers import CompanySerializer
from rest_framework import status

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def create_api(request,pk=None):
    if request.method=='GET':

        id=pk
        if id is not None:
            com=CompanyDetails.objects.get(id=id)
            serializer=CompanySerializer(com)
            return Response(serializer.data)
        com=CompanyDetails.objects.all()
        serializer=CompanySerializer(com,many=True)
        return Response(serializer.data)
    
    if request.method=='POST':
        serializer=CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    if request.method=='PUT':
        id=pk
        com=CompanyDetails.objects.get(pk=id)
        serializer=CompanySerializer(com,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
    
    if request.method=='PATCH':
        id=pk
        com=CompanyDetails.objects.get(pk=id)
        serializer=CompanySerializer(com,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors)
    
    if request.method=='DELETE':
        id=pk
        com=CompanyDetails.objects.get(pk=id)
        com.delete()
        return Response({'msg':'Data Deleted'})
