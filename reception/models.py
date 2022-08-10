from django.db import models
from django.contrib.auth.models import AbstractUser,User

class PatientProfile(AbstractUser):

    patient_id = models.ForeignKey(User,on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=30, null=True)
    patient_gender = models.CharField(max_length=10, null=True)
    patient_phone = models.IntegerField(null=True)
    patient_dob = models.DateField(max_length=200, null=True)
    patient_password = models.CharField(max_length=50, null=True)

    def __str__(self):
        return str(self.patient_id)

class UserRole(AbstractUser):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    user_role = models.CharField(max_length=10)

    def __str__(self):
        return str(self.user_id)

class DoctorProfile(AbstractUser):
    doctor_id = models.ForeignKey(User,on_delete=models.CASCADE)
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