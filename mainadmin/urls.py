from django.urls import path
from .import views

urlpatterns=[

    path('addtrainer',views.add_trainer,name="add_trainer"),
    path('adduser',views.add_user,name='add_user'),
    path('createpackage',views.create_package,name='create_package')

]