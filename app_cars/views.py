from django.shortcuts import render, redirect

from .forms import *
from .models import *


# Create your views here.
def index(request):
    data = Car.objects.all()
    specdata = Specifications.objects.all()
    form = AddCar()

    return render(request, 'index.html', {'data': data, 'specdata': specdata, 'form': form})


def add_car(request):
    form = AddCar(request.POST)

    if form.is_valid():
        form.save()
        return redirect('/')


def add_specs(request, car_id):
    data = Car.objects.all()
    formspecs = AddSpecifications()

    return render(request, 'add_specs.html', {'formspecs': formspecs, 'data': data})


def update_specs(request):
    form = AddSpecifications(request.POST)

    if form.is_valid():
        form.save()
        return redirect('/')


def delete_car(request, car_id):
    data = Car.objects.get(id=car_id)
    data.delete()
    return redirect('/')
