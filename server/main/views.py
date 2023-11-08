from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html')

def update_schedule(request):
    return render(request, 'main/update_schedule.html')