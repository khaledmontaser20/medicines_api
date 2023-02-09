from itertools import product
from rest_framework import serializers
from django.shortcuts import get_object_or_404
from .models import Medicine


class MedicineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Medicine
        fields = "__all__"
        read_only_fields = ['id']
