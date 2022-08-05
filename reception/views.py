from django.shortcuts import render
import random
from .models import *

# Create your views here.
def reception(request):
    random_id = 'P'+''.join([str(random.randint(0, 999)).zfill(3) for _ in range(2)])
    query = PatientDetail.objects.filter(patient_id==random_id)
    if (request.method=='POST'):
        if query:
            patient_id = random_id
            patient_name = request.POST.get('pname')
            patient_gender = request.POST.get('gender')
            patient_dob = request.POST.get('dob')
            patient_phone = request.POST.get('mob')

    return render(request, 'reception.html')

def register_doctor(request):
    return render(request, 'registerdoctor.html')