from django.db import models

class PatientDetail(models.Model):
    patient_id = models.CharField(max_length=200, unique=True)
    patient_name = models.CharField(max_length=50)
    patient_gender = models.CharField(max_length=10)
    patient_dob = models.DateField()
    patient_phone = models.CharField(max_length=20)

    def __str__(self):
        return str(self.patient_id)

class DoctorDetail(models.Model):
    doctor_id = models.CharField(max_length=200, unique=True)
    doctor_name = models.CharField(max_length=50)
    doctor_image = models.ImageField(upload_to='doctor_img/')
    doctor_dob = models.DateField()
    doctor_gender = models.CharField(max_length=10)
    doctor_phone = models.CharField(max_length=20)
    doctor_address = models.CharField(max_length=200)
    doctor_department = models.CharField(max_length=100)
    doctor_qualification = models.CharField(max_length=100)
     
    def __str__(self):
        return str(self.doctor_id)