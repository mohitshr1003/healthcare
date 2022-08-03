from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('doctor-login/', doctor_login),
    path('patient-login/', patient_login),
]
