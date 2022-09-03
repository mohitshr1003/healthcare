from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class PatientDetail(models.Model):

    patient_name = models.CharField(max_length=30)
    patient_id = models.ForeignKey(User, on_delete=models.CASCADE)
    patient_gender = models.CharField(max_length=10)
    patient_mail = models.EmailField()
    patient_dob = models.DateField()
    patient_dep = models.CharField(max_length=30)
    patient_password = models.CharField(max_length=100)

    def mohit(self, *args, **kwargs):
        post_save.send(PatientDetail, instance=self, created=True, pwd=args[0])
        super(PatientDetail, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.patient_id)

class Department(models.Model):
    department_name = models.CharField(max_length=30,unique=True)

    def __str__(self):
        return self.department_name

class DoctorDetail(models.Model):
    doctor_id = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor_name = models.CharField(max_length=30)
    doctor_image = models.ImageField(upload_to='doctor_img/')
    doctor_dob = models.DateField()
    doctor_gender = models.CharField(max_length=10)
    doctor_mail = models.EmailField()
    doctor_address = models.CharField(max_length=200)
    doctor_department = models.CharField(max_length=30)
    doctor_qualification = models.CharField(max_length=100)
    doctor_password = models.CharField(max_length=100)
     
    def __str__(self):
        return str(self.doctor_id)

class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=30)
     
    def __str__(self):
        return str(self.role)