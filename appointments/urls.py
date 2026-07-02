from rest_framework.routers import DefaultRouter
from django.urls import path, include
from appointments.views import QuoteViewSet, DiagnosisViewSet

router = DefaultRouter()

router.register('quote', QuoteViewSet)

router.register('diagnosis', DiagnosisViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
