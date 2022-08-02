from django.urls import path
from .views import *

urlpatterns = [
    path('reception/', reception),
    path('reception/doctor/', register_doctor)
]
