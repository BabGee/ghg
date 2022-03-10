from django.shortcuts import render

def index(request):
    return render(request, 'ghg_measure/dashboard.html')