from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index),
    path('doctor-login/', doctor_login),
]
