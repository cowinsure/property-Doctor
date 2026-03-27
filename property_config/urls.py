from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PropertyConfigViewSet

router = DefaultRouter()
router.register(r'property-config', PropertyConfigViewSet, basename='property-config')

urlpatterns = [
    path('', include(router.urls)),
]
