from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Cricketer, Role, Type
from datetime import date
from django.db.models import Q

# Create your views here.

def index(request):
    return render(request, 'index.html')


def all_cricketer(request):
    cricketers = Cricketer.objects.all()
    context = {
        'cricketers' : cricketers
    }
    return render(request, 'view_all_cricketer.html', context)


def add_cricketer(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        birth_date = request.POST['birth_date']
        matches_played = int(request.POST['matches_played'])
        match_allowance = int(request.POST['match_allowance'])
        phone = int(request.POST['phone'])
        role = str(request.POST['role'])
        type = str(request.POST['type'])
        new_cricketer = Cricketer(first_name=first_name, last_name=last_name, birth_date=birth_date, matches_played=matches_played,match_allowance=match_allowance, phone=phone, role_id=role, type_id=type)
        new_cricketer.save()
        return HttpResponse('Cricketer Added Successfully')

    elif request.method=='GET':
        return render(request, 'add_cricketer.html')

    else:
        return HttpResponse("Error Occurred While Adding Cricketer")


def remove_cricketer(request, cricketer_id = 0):
    if cricketer_id:
        try:
            cricketer_to_be_removed = Cricketer.objects.get(id=cricketer_id)
            cricketer_to_be_removed.delete()
            return HttpResponse("Cricketer Removed Successfully")
        except:
            return HttpResponse("Please Enter A Valid Cricketer ID")
    cricketers = Cricketer.objects.all()
    context = {
        'cricketers':cricketers
    }
    return render(request, 'remove_cricketer.html', context)


def filter_cricketer(request):
    if request.method == 'POST':
        name = request.POST['name']
        role = request.POST['role']
        type = request.POST['type']
        cricketers = Cricketer.objects.all()
        if name:
            cricketers = cricketers.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if role:
            cricketers = cricketers.filter(role__name__icontains = role)
        if type:
            cricketers = cricketers.filter(type__name__icontains = type)

        context = {
            'cricketers' : cricketers
        }

        return render(request, 'view_all_cricketer.html', context)

    elif request.method == 'GET':
        return render(request, 'filter_cricketer.html')

    else:
        return HttpResponse('An Exception Occured')