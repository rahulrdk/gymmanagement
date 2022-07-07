from django.shortcuts import render
from django.http import HttpResponse

def logindef(request):
    return render(request,'user/login.html')

def homepagedef(request):
    return render(request,'user/homepage.html')

def paymentdef(request):
    return render(request,'user/payment.html')

def planselectiondef(request):
    return render(request,'user/planselection.html')

# Create your views here.
