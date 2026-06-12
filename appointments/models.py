from django.db import models
from users.models import User, Post

# Create your models here.
class Quote(models.Model):

    # Values for the states
    STATE_CHOICES = [
        ('pending', 'Pendiente'),
        ('confirmed', 'Confirmada'),
        ('cancelled', 'Cancelada'),
        ('completed', 'Completada')
    ]

    patient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='quote_patient'
    )

    doctor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='quote_doctor'
    )

    # By default, any appointment starts in pending status
    state = models.CharField(max_length=20, choices=STATE_CHOICES, default='pending')

    # Specialty of the appointment
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='quote_post'
    )

    description = models.TextField(blank=True, null=True)

    appointment_date = models.DateTimeField()

    class Meta:
        db_table = 'quote'

    def __str__(self):
        return f'{self.patient} - {self.doctor} - {self.appointment_date}'

class Diagnosis(models.Model):

    # OneToOneField => Just having a diagnosis
    quote = models.OneToOneField(
        Quote,
        on_delete=models.CASCADE,
        related_name='diagnosis_quote'
    )

    doctor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='diagnosis_doctor'
    )

    summary = models.TextField(blank=True, null=True)

    #  auto_now_add => current date automatically
    date_of_diagnosis = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Table name
        db_table = 'diagnosis'

    def __str__(self):
        return f'{self.quote} - {self.doctor} - {self.date_of_diagnosis}'
