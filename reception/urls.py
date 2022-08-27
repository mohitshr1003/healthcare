from django.urls import path
from .views import *

urlpatterns = [
    path('reception/', reception),
    path('reception/doctor/', register_doctor),
    path('reception/department/',department_name),
    path('reception/doctor-list/',doctor_details)
]
