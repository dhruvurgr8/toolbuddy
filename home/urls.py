from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('imagetotext',views.imagetotext,name='imagetotext'),
    path('image',views.image,name='image')

]


