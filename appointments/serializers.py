from rest_framework import serializers
from appointments.models import Quote, Diagnosis
from users.serializers import UserSerializer, PostSerializer

class QuoteSerializer(serializers.ModelSerializer):
    patient = UserSerializer(read_only=True)
    doctor = UserSerializer(read_only=True)
    post = PostSerializer(read_only=True)

    class Meta:
        model = Quote
        fields = '__all__'

class DiagnosisSerializer(serializers.ModelSerializer):
    quote = QuoteSerializer(read_only=True)
    doctor = UserSerializer(read_only=True)

    class Meta:
        model = Diagnosis
        fields = '__all__'
