from django.shortcuts import render
from .models import Account
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.hashers import make_password
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method=="POST":
        act=Account.objects.create(email=request.POST.get('email'),contact_number=request.POST.get('contact number'),password=make_password(request.POST.get('password')))
        return render(request,"EmailAuth/SignIn.html")
    return render(request,"EmailAuth/SignUp.html")

def logIn(request):
    if request.method=="POST":
        user=auth.authenticate(email=request.POST.get('email'),password=request.POST.get('password'))
        if user is not None:
            auth.login(request,user)
            return render(request,'EmailAuth/Home.html',{"email":request.POST.get("email")})
        else:
            return HttpResponseRedirect('/logIn')
    else:
        return render(request,"EmailAuth/SignIn.html")


def power(x,i):
    if i==1:
        return x
    else:
        return x*power(x,i-1)
def sigma(x,n):
    res=0
    for i in range(1,n+1):
        res=res+(1/power(x,i))
    return res

@login_required(login_url='/login')
def calculate_qstn1(APIView):
    def post(self,request):
        x=request.POST.get('x')
        n=request.POST.get('n')
        res=sigma(x,n)
        data={'res':res}
        return JsonResponse(data)

def calculate(request):
    return render(request,"EmailAuth/calculate.html")

