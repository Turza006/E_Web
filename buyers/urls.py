from django.urls import path, include
from . import views

urlpatterns = [
    path('buysignup', views.bsignup, name='buysignup'),
    path('buylogin', views.blogin, name='buylogin'),
    path('buylogout', views.blogout, name='buylogout'),
]