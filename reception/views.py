from django.shortcuts import render

# Create your views here.
def reception(request):
    return render(request, 'reception.html')