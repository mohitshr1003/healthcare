from django.shortcuts import render
import string as s
import random
from .models import *
from django.contrib import messages


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
            patient_password = p_password
        )
        patient_registration.save()
        messages.success(request, f'Patient account is created successfully')
    return render(request, 'reception.html')

def register_doctor(request):
    return render(request, 'registerdoctor.html')
