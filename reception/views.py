from django.shortcuts import render

# Create your views here.
def reception(request):
    return render(request, 'reception.html')

def register_doctor(request):
    return render(request, 'registerdoctor.html')