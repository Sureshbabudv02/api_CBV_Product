from django.shortcuts import render

# Create your views here.
from app.serializers import *
from rest_framework.decorators import APIView
from rest_framework.response import Response

class ProductCrud(APIView):
    def get(self,request):
        POD = Product.objects.all()
        JOD = ProductModelSerializer(POD,many=True)
        return Response(JOD.data)
    
    def post(self,request):
        POD = ProductModelSerializer(data=request.data)

        if POD.is_valid():
            POD.save()
            return Response({'insert':'Inserted Successfully'})
        else:
            return Response({'Error':'Error'})