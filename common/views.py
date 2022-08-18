from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def common_login(request):
    return render(request,'common/login.html')

def main_page(request):
    return render(request,'common/mainpage.html')

