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
    alpha_id = random.choices(s.ascii_uppercase, k=N)  # ABH254
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
            patient_name=p_name,
            patient_id=p_id,
            patient_gender=p_gender,
            patient_phone=p_mob,
            patient_dob=p_dob,
            patient_password=make_password(p_password)
        )
        user = User.objects.create_user(
            p_id,
            None,
            p_password
            )
        user.save()
    return render(request, 'reception.html')


def register_doctor(request):
    return render(request, 'registerdoctor.html')
