from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('doctor-login/', doctor_login),
    path('patient-login/', patient_login),
    path('doctor-dashboard/', doctor_dashboard),
    path('patient-dashboard/', patient_dashboard),
    path('logout/', log_out),
]
