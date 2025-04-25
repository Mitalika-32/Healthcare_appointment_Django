from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Doctor(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField(unique=True)
	password = models.CharField(max_length=16)
	gender = models.CharField(max_length=10)
	phonenumber = models.CharField(max_length=10)
	address = models.CharField(max_length=100)
	birthdate = models.DateField()
	bloodgroup = models.CharField(max_length=5)
	specialization = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Receptionist(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField(unique=True)
	password = models.CharField(max_length=16)
	gender = models.CharField(max_length=10)
	phonenumber = models.CharField(max_length=10)
	address = models.CharField(max_length=100)
	birthdate = models.DateField()
	bloodgroup = models.CharField(max_length=5)

	def __str__(self):
		return self.name

class Patient(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField(unique=True)
	password = models.CharField(max_length=16)
	gender = models.CharField(max_length=10)
	phonenumber = models.CharField(max_length=10)
	address = models.CharField(max_length=100)
	birthdate = models.DateField()
	bloodgroup = models.CharField(max_length=5)

	def __str__(self):
		return self.name

class Appointment(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Declined', 'Declined'),
    )

    doctorname = models.CharField(max_length=50)
    doctoremail = models.EmailField(max_length=50)
    patientname = models.CharField(max_length=50)
    patientemail = models.EmailField(max_length=50)
    appointmentdate = models.DateField(max_length=10)
    appointmenttime = models.TimeField(max_length=10)
    symptoms = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    prescription = models.CharField(max_length=200,blank=True, null=True)

    def __str__(self):
        return f"{self.patientname} with {self.doctorname} on {self.appointmentdate}"
	
# sitehandler/models.py

class Prescription(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE,related_name='appointment_prescription',null=True,blank=True)
    symptoms = models.TextField(null=True, blank=True)
    diagnosis = models.TextField()
    medication = models.TextField(null= True,blank=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Prescription for {self.appointment.patientname} by {self.appointment.doctorname}"





