from itertools import product
from rest_framework import serializers
from django.shortcuts import get_object_or_404
from .models import Medicine
from urllib.parse import unquote


class MedicineSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    # def get_image(self, obj):
    #     if obj.image:
    #         return unquote(obj.image.url)
    #     return None
    
    def get_image(self, obj):
        if obj.image:
            image_url = unquote(obj.image.url)
            if image_url.startswith('/media/'):
                image_url = image_url[len('/media/'):]
            return image_url
        return None

    class Meta:
        model = Medicine
        fields = "__all__"
        read_only_fields = ['id']


class OCRSerializer(serializers.Serializer):
    image = serializers.ImageField()