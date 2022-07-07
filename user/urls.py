from django.urls import path
from .import views

urlpatterns = [
    path('',views.logindef,name='login'),
    path('Home page',views.homepagedef,name='Homepage'),
    path('plan selection',views.planselectiondef,name='planselection'),
    path('payment',views.paymentdef,name='payment'),
]