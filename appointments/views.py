from rest_framework import viewsets
from appointments.models import Diagnosis, Quote
from appointments.serializers import DiagnosisSerializer, QuoteSerializer
from users.permissions import (IsDoctor, IsPatient)


# Create your views here.
class DiagnosisViewSet(viewsets.ModelViewSet):
    queryset = Diagnosis.objects.all()
    serializer_class = DiagnosisSerializer
    permission_classes = [IsDoctor]

class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [IsDoctor | IsPatient]
