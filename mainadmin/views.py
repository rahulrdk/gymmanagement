from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def add_trainer(request):
    return render(request,'mainadmin/add_trainer.html')

def add_user(request):
    return render(request,'mainadmin/add_user.html')

def create_package(request):
    return render(request,'mainadmin/create_package.html')