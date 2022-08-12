from django.db import models
from django.contrib.auth.models import User
class PatientDetail(models.Model):

    patient_name = models.CharField(max_length=30)
    patient_id = models.ForeignKey(User, on_delete=models.CASCADE)
    patient_gender = models.CharField(max_length=10)
    patient_phone = models.IntegerField()
    patient_dob = models.DateField()
    patient_password = models.CharField(max_length=100)

    def __str__(self):
        return str(self.patient_id)

class DoctorDetail(models.Model):
    doctor_id = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor_name = models.CharField(max_length=30)
    doctor_image = models.ImageField(upload_to='doctor_img/')
    doctor_dob = models.DateField()
    doctor_gender = models.CharField(max_length=10)
    doctor_phone = models.IntegerField()
    doctor_address = models.CharField(max_length=200)
    doctor_department = models.CharField(max_length=100)
    doctor_qualification = models.CharField(max_length=100)
    doctor_password = models.CharField(max_length=100)
     
    def __str__(self):
        return str(self.doctor_id)

class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=30)
     
    def __str__(self):
        return str(self.role)