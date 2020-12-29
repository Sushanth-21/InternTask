from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('graph/', views.graph, name='graph'),
    path('cal_graph/', views.cal_graph, name='cal_graph'),
]
