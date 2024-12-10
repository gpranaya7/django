from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from app.serializers import *
from rest_framework.response import Response
# Create your views here.
class productsView_set(ViewSet):
    def list(self,request):
        lpo=products.objects.all()
        spo=SerializedProducts(lpo,many=True)
        return Response(spo.data)
    def retrieve(self,request,pk):
        ipo=products.objects.get(pid=pk)
        spo=SerializedProducts(ipo)
        return Response(spo.data)
    def create(self,request):
        spo=SerializedProducts(data=request.data)
        if spo.is_valid():
            spo.save()
            return Response({"create":"data is inserted"})
        else:
            return Response({'error':'data is not inserted'})
    def update(self,request,pk):
        ipo=products.objects.get(pid=pk)
        spo=SerializedProducts(ipo,data=request.data)
        if spo.is_valid():
            spo.save()
            return Response({'update':'the data is updated'})
        else:
            return Response({'update':'data is not updated'})
    
    def partial_update(self,request,pk):
        ipo=products.objects.get(pid=pk)
        spo=SerializedProducts(ipo,data=request.data,partial=True)
        if spo.is_valid():
            spo.save()
            return Response({'update':'update is done'})
        else:
            return Response({'update':'update is not done'})
    def destroy(self,request,pk):
        ipo=products.objects.get(pid=pk)
        ipo.delete()
        return Response({'delete':'deleted'})



    
