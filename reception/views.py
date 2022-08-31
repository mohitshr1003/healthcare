from pydoc import doc
from django.shortcuts import render
import string as s
import random
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse

def p_gen_id_pswd():
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
    check_id = User.objects.filter(username=p_id)

    if check_id:
        p_gen_id_pswd()

    return p_id,p_password

def reception(request):

    if(request.method == 'POST'):

        p_id, p_pass = p_gen_id_pswd()
        print(p_id)
        print(p_pass)

        user = User.objects.create_user(
            p_id,
            None,
            p_pass
            )

        p_name = request.POST.get('pname')
        p_gender = request.POST.get('pgender')
        p_dob = request.POST.get('pdob')
        p_dep = request.POST.get('department')
        p_mob = request.POST.get('pmob')

        patient_registration = PatientDetail(
            patient_name=p_name,
            patient_id=user,
            patient_gender=p_gender,
            patient_phone=p_mob,
            patient_dep = p_dep,
            patient_dob=p_dob,
            patient_password=make_password(p_pass)
        )
        patient_registration.save()

        user_role = UserRole(
            user = user,
            role = "Patient"
        )
        user_role.save()

    return render(request, 'reception.html')


def d_gen_id_pswd():
    # for DOCTOR ID
    N = 3
    # alpha_id = list('DOC')
    num_id = random.choices(s.digits, k=N)
    d_id = str(''.join(list("DOC") + num_id))

    # for DOCTOR PASSWORD
    M = 10

    d_password = str(
        ''.join(
            random.choices(
                s.ascii_letters + s.digits + "#$%@!(){}[]-", k=M
                )
            )
    )

    check_id = User.objects.filter(username=d_id)

    if check_id:
        d_gen_id_pswd()

    return d_id, d_password

def register_doctor(request):

    if (request.method=="POST"):

        d_id, d_password = d_gen_id_pswd()
        print(d_id)
        print(d_password)

        user = User.objects.create_user(
            d_id, 
            None, 
            d_password
            )
        
        d_name = request.POST.get('dname')
        d_image = request.FILES.get('dimg')
        d_dob = request.POST.get('ddob')
        d_gender = request.POST.get('dgender')
        d_phone = request.POST.get('dmob')
        d_address = request.POST.get('daddress')
        d_department = request.POST.get('department')
        d_qualification = request.POST.get('qualification')

        doctor_registration = DoctorDetail(
            doctor_id = user,
            doctor_name = d_name,
            doctor_image = d_image,
            doctor_dob = d_dob,
            doctor_gender = d_gender,
            doctor_phone = d_phone,
            doctor_address = d_address,
            doctor_department = d_department,
            doctor_qualification = d_qualification,
            doctor_password = make_password(d_password)
        )
        doctor_registration.save()

        user_role = UserRole(
            user = user,
            role = "Doctor"
        )
        user_role.save()
    return render(request, 'registerdoctor.html')


def department_name(request):
    data = Department.objects.all()
    final_data = []
    for d in data:
        final_data.append(d.department_name)

    return JsonResponse(final_data, safe=False)
        
def doctor_details(request):
    get_dep = request.GET.get('dep_name')
    doc_data = None
    doc_list = []
    if get_dep:
        doc_data = DoctorDetail.objects.filter(doctor_department=get_dep)
    if doc_data:
        for i in doc_data:
            doc_dict = {}
            doc_dict['name']=i.doctor_name
            doc_list.append(doc_dict)
    return JsonResponse(doc_list,safe=False)

def patient_details(request):
    patient_name = request.GET.get('p_name')
    patient_data = None
    if patient_name:
        patient_data = PatientDetail.objects.filter(patient_name__contains=patient_name)
    p_list = []
    if patient_data:
        for i in patient_data:
            p_dict = {}
            p_dict['name']=i.patient_name
            p_list.append(p_dict)
    return JsonResponse(p_list,safe=False)