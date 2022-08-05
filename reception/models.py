from django.db import models
class PatientDetails(models.Model):

    patient_name = models.CharField(max_length=30, null=True)
    patient_id = models.CharField(max_length=6, null=True)
    patient_gender = models.CharField(max_length=10, null=True)
    patient_phone = models.IntegerField(null=True)
    patient_dob = models.DateField(max_length=200, null=True)
    patient_password = models.CharField(max_length=50, null=True)

    def __str__(self):
        return str(self.patient_id)

class DoctorDetail(models.Model):
    doctor_id = models.CharField(max_length=6, unique=True)
    doctor_name = models.CharField(max_length=30)
    doctor_image = models.ImageField(upload_to='doctor_img/')
    doctor_dob = models.DateField()
    doctor_gender = models.CharField(max_length=10)
    doctor_phone = models.IntegerField()
    doctor_address = models.CharField(max_length=200)
    doctor_department = models.CharField(max_length=100)
    doctor_qualification = models.CharField(max_length=100)
     
    def __str__(self):
        return str(self.doctor_id)