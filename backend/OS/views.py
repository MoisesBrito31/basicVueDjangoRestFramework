from rest_framework import generics
from .serializer import OsSerializer
from .models import OS

class OsList(generics.ListCreateAPIView):
    queryset = OS.objects.all()
    serializer_class = OsSerializer

class OsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OS.objects.all()
    serializer_class = OsSerializer
    
