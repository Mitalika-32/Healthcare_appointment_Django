from django import forms
from .models import Prescription

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['symptoms', 'diagnosis', 'medication', 'notes']  # Make sure these match model fields exactly
