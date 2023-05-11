from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializer import OsSerializer
from .models import OS
from time import sleep

class OsList(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        queryset = OS.objects.all()
        serial = OsSerializer(queryset,many=True)
        return Response(serial.data)
    def post(self,request):
        serial = OsSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class OsDetail(APIView):  
    permission_classes=[IsAuthenticated]
    def get(self,request,pk):
        try:
            obj = OS.objects.get(id=pk)
            serial = OsSerializer(obj)
            return Response(serial.data)
        except Exception as EX:
            return Response(str(EX),status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def post(self,request,pk):
        obj = OS.objects.get(id=pk)
        serial = OsSerializer(obj,data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def delete(self, request, pk):
        try:
            obj = OS.objects.get(id=pk)
            obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as EX:
            return Response(str(EX),status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
