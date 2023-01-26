
from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('',views.image2pdf,name='image2pdf'),


    ]

