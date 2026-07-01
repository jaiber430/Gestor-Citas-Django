from rest_framework import viewsets
from appointments.models import Diagnosis, Quote
from appointments.serializers import DiagnosisSerializer, QuoteSerializer

# Create your views here.
class DiagnosisViewSet(viewsets.ModelViewSet):
    queryset = Diagnosis.objects.all()
    serializer_class = DiagnosisSerializer

class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
