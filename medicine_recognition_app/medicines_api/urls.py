from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('medicine', views.MedicineViewset)
app_name = 'medicines_api'

urlpatterns = [
    path('', include(router.urls)),
    path('ocr/', views.OCRView.as_view(), name='ocr'),
]
