from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request,'user/homepage.html')

def payment(request):
    return render(request,'user/payment.html')

def plan_selection(request):
    return render(request,'user/planselection.html')

# Create your views here.
