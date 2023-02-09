from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from medicines_api import views

router = DefaultRouter()
router.register('medicine', views.MedicineViewset)
app_name = 'medicines_api'

urlpatterns = [
    path('', include(router.urls)),
]
