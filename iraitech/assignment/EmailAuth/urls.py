from django.urls import path
from .views import register,logIn,calculate_qstn1,calculate

urlpatterns = [
    path('SignIn/', register,name="SignUp"),
    path('logIn/', logIn,name="logIn"),
    path('api/v1/calculate/',calculate_qstn1,name="calculate"),
    path('calculate/',calculate),
]