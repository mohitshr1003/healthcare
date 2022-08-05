from django.shortcuts import render
import string as s
import random
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


# Create your views here.
def reception(request):
    
    # for USER ID
    N = 3
    alpha_id = random.choices(s.ascii_uppercase, k=N)
    num_id = random.choices(s.digits, k=N)
    p_id = str(''.join(alpha_id + num_id))

    # for USER PASSWORD
    M = 8

    p_password = str(
        ''.join(
            random.choices(
                s.ascii_letters + s.digits + "#$%@!(){}[]-", k=M
                )
            )
    )
    print(p_id)
    print(p_password)

    if(request.method == 'POST'):
        p_name = request.POST.get('pname')
        p_gender = request.POST.get('pgender')
        p_dob = request.POST.get('pdob')
        p_mob = request.POST.get('pmob')

        patient_registration = PatientDetails(
            patient_name = p_name,
            patient_id = p_id,
            patient_gender = p_gender,
            patient_phone = p_mob,
            patient_dob = p_dob,
            patient_password = make_password(p_password)
        )
        patient_registration.save()
        user = User.objects.create_user(
            p_id, 
            None, 
            p_password
            )
        user.save()   
    return render(request, 'reception.html')

def register_doctor(request):
    # for DOCTOR ID
    N = 3
    alpha_id = list('Doc')
    num_id = random.choices(s.digits, k=N)
    d_id = str(''.join(alpha_id + num_id))

    # for DOCTOR PASSWORD
    M = 10

    d_password = str(
        ''.join(
            random.choices(
                s.ascii_letters + s.digits + "#$%@!(){}[]-", k=M
                )
            )
    )
    print(d_id)
    print(d_password)

    if (request.method=="POST"):
        d_name = request.POST.get('dname')
        d_image = request.FILES.get('dimg')
        d_dob = request.POST.get('ddob')
        d_gender = request.POST.get('dgender')
        d_phone = request.POST.get('dmob')
        d_address = request.POST.get('daddress')
        d_department = request.POST.get('department')
        d_qualification = request.POST.get('qualification')

        doctor_registration = DoctorDetail(
            doctor_id = d_id,
            doctor_name = d_name,
            doctor_image = d_image,
            doctor_dob = d_dob,
            doctor_gender = d_gender,
            doctor_phone = d_phone,
            doctor_address = d_address,
            doctor_department = d_department,
            doctor_qualification = d_qualification
        )
        doctor_registration.save()
        user = User.objects.create_user(
            d_id, 
            None, 
            d_password
            )
        user.save()
    return render(request, 'registerdoctor.html')
