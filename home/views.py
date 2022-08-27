from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from reception.models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'index.html')

def doctor_login(request):

    data = {}
    # p_login = PatientDetails
    if(request.method == "POST"): 
        username = request.POST.get("doctor_id") 
        password = request.POST.get("psw")
        
        user = authenticate(username=username, password=password)
        if user is not None:
            user_role = UserRole.objects.filter(user=user).first()
            role = user_role.role
            if role == "Doctor":

                login(request, user)
                return redirect(doctor_dashboard)
    return render(request, 'doctor-login.html')

def patient_login(request):

    # p_login = PatientDetails
    if(request.method == "POST"): 
        username = request.POST.get("patient_id") 
        password = request.POST.get("psw")

        user = authenticate(username=username, password=password)
        if user is not None:
            user_role = UserRole.objects.filter(user=user).first()
            role = user_role.role
            if role == "Patient":
                login(request, user)
                return redirect(patient_dashboard)
    return render(request, 'patient-login.html')

@login_required(login_url='/doctor-login')
def doctor_dashboard(request):
    return render(request, 'doctor-dashboard.html')


@login_required(login_url='/patient-login')
def patient_dashboard(request):
    return render(request, 'patient-dashboard.html')

def log_out(request):
    logout(request)
    return redirect(index)