from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import AutoMpgFile, AutoMpgData
from plotly.offline import plot
from plotly.graph_objs import Scatter
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
import json


def register(request):
    if request.user.is_authenticated:
        return redirect("/graph/graph/")
    else:
        if request.method == 'POST':
            if request.POST['password'] != request.POST['confirm password']:
                messages.warning(request, f'ERROR : Passwords did not match')
            else:
                try:
                    User.objects.create_user(
                        request.POST['username'], request.POST['email'], request.POST['password'])
                    return render(request, 'graph/login.html')
                except:
                    messages.warning(request, f'ERROR : User already exists')
        return render(request, 'graph/register.html')


def login_user(request):
    if request.user.is_authenticated:
        return redirect("/graph/graph/")
    else:
        if request.method == "POST":
            user = authenticate(
                username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                login(request, user)
                return redirect('/graph/graph/')
            else:
                messages.warning(request, "Invalid username or password.")
                return render(request, 'graph/login.html')

        else:
            return render(request, 'graph/login.html')


def graph(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            mpg_file = AutoMpgFile.objects.create(
                user=request.user, mpg_file=request.FILES['auto-mpg'])
            mpg_file.save()
            f = open(mpg_file.mpg_file.path, 'r')
            l1 = f.readlines()
            dw = {}
            dm = {}
            for i in l1:
                mpg_data = AutoMpgData.objects.create(data_file=mpg_file)
                l = i.split()
                s = ''
                for i in range(8, len(l)):
                    s = s+' '+l[i]
                s = s.strip()
                l[8] = s[1:len(s)-1]
                l = l[:9]
                if l[0] == '?':
                    mpg_data.mpg = None
                else:
                    mpg_data.mpg = float(l[0])
                if l[1] == '?':
                    mpg_data.cylinders = None
                else:
                    mpg_data.cylinders = int(l[1])
                if l[2] == '?':
                    mpg_data.displacement = None
                else:
                    mpg_data.displacement = float(l[2])
                if l[3] == '?':
                    mpg_data.horsepower = None
                else:
                    mpg_data.horsepower = float(l[3])
                if l[4] == '?':
                    mpg_data.weight = None
                else:
                    mpg_data.weight = float(l[4])
                if l[5] == '?':
                    mpg_data.acceleration = None
                else:
                    mpg_data.acceleration = float(l[5])
                if l[6] == '?':
                    mpg_data.model_year = None
                else:
                    mpg_data.model_year = int(l[6])
                if l[7] == '?':
                    mpg_data.origin = None
                else:
                    mpg_data.origin = int(l[7])
                if l[8] == '?':
                    mpg_data.car_name = None
                else:
                    mpg_data.car_name = l[8]
                mpg_data.save()
                if l[4] == '?':
                    c = 0.0
                else:
                    c = float(l[4])
                if l[8] in dw.keys():
                    dw[l[8]].append(c)
                else:
                    dw[l[8]] = list([c])
                if l[0] == '?':
                    c = 0.0
                else:
                    c = float(l[0])
                if l[8] in dm.keys():
                    dm[l[8]].append(c)
                else:
                    dm[l[8]] = list([c])
            f.close()
            lwy = []
            lmy = []
            lx = []
            for i in dw:
                if len(dw[i]) > 1:
                    if i not in lx:
                        lx.append(i)
                        lwy.append((sum(dw[i])/len(dw[i])))
                        lmy.append((sum(dm[i])/len(dm[i])))
            plot_div = plot([Scatter(x=lx, y=lwy)],
                            output_type='div', include_plotlyjs=False)

            lx = json.dumps(lx)
            lmy = json.dumps(lmy)
            lwy = json.dumps(lwy)

            data = {'plot_div': plot_div, 'lx': lx,
                    'lmy': lmy, 'lwy': lwy, 'name': True}
            return render(request, 'graph/graph.html', data)
        else:
            return render(request, 'graph/graph.html', {'plot_div': '', 'name': False})
    else:
        return redirect('/graph/login/?next=/graph/')


@csrf_exempt
def cal_graph(request):
    if request.method == 'POST':
        lx = request.POST.getlist("lx[]")
        lwy = request.POST.getlist("lwy[]")
        lmy = request.POST.getlist("lmy[]")
        for i in range(len(lwy)):
            lwy[i] = float(lwy[i])
        for i in range(len(lmy)):
            lmy[i] = float(lmy[i])
        data = {'lx': lx,
                'lmy': lmy, 'lwy': lwy}
        if 'avg-mpg' in request.POST:
            name = True
            plot_div = plot([Scatter(x=lx, y=lmy)],
                            output_type='div', include_plotlyjs=False)
            data['plot_div'] = plot_div
            data['name'] = name
        if 'avg-wt' in request.POST:
            name = False
            plot_div = plot([Scatter(x=lx, y=lwy)],
                            output_type='div', include_plotlyjs=False)
            data['plot_div'] = plot_div
            data['name'] = name
        lx = json.dumps(lx)
        lmy = json.dumps(lmy)
        lwy = json.dumps(lwy)
        plot_div = json.dumps(plot_div)
        data = {'plot_div': plot_div, 'lx': lx,
                'lwy': lwy, 'lmy': lmy, 'name': name}
        return JsonResponse(data)


def logout_user(request):
    if request.method == "POST":
        logout(request)
        messages.success(request, "Logged out successfully!")
        return redirect('/graph/login/')
    else:
        if request.user.is_authenticated:
            return redirect('/graph/graph/')
        else:
            return redirect('/graph/login/')
