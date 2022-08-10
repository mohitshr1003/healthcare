from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from reception.models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def doctor_login(request):
    return render(request, 'doctor-login.html')

def patient_login(request):

    # p_login = PatientDetails
    if(request.method == "POST"): 
        username = request.POST.get("patient_id") 
        password = request.POST.get("psw")

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(index)
        else:
            return render(request, 'patient-login.html')

    return render(request, 'patient-login.html')