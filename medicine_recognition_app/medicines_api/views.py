from django.shortcuts import render
from .models import Medicine
from rest_framework import viewsets, filters
from .serializers import MedicineSerializer

# Create your views here.


class MedicineViewset(viewsets.ModelViewSet):
    queryset = Medicine.objects.all().order_by("id")
    serializer_class = MedicineSerializer
