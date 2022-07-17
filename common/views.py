from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def common_login(request):
    return render(request,'common/login.html')

