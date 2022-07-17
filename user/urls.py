from django.urls import path
from .import views

urlpatterns = [

    path('Homepage',views.home,name='Homepage'),
    path('plan-selection',views.plan_selection,name='plan_selection'),
    path('payment',views.payment,name='payment'),

]