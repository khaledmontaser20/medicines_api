from django.shortcuts import render
from .models import Medicine
from rest_framework import viewsets, filters, generics
from .serializers import MedicineSerializer

from rest_framework.response import Response
import easyocr
from .serializers import OCRSerializer
from rest_framework import filters

# Create your views here.


class MedicineViewset(viewsets.ModelViewSet):
    queryset = Medicine.objects.all().order_by("id")
    serializer_class = MedicineSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['en_name', 'ar_name']



from io import BytesIO
from PIL import Image
import numpy as np

class OCRView(generics.CreateAPIView):
    serializer_class = OCRSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Convert image data into numpy array
        image_data = serializer.validated_data['image'].read()
        image = np.array(Image.open(BytesIO(image_data)).convert('RGB'))

        reader = easyocr.Reader(['en'])
        result = reader.readtext(image)

        maxH = 0
        dictOfHeights = {}
        for word in result:
            height = int(word[0][3][1]) - int(word[0][0][1])
            dictOfHeights[word[1]] = height
            maxH = max(maxH, height)

        for k, v in dictOfHeights.items():
            if v == maxH:
                output = k
                break

        return Response({'output': output})

