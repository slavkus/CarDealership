from django import forms
from django.forms import ModelForm
from .models import *


class DisplayCar(ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class AddCar(ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        widgets = {
            'brand': forms.TextInput(),
            'name': forms.TextInput(),
            'date_of_release': forms.DateInput(attrs={'type': 'date'}, format='%d-%m-%y'),
            'initial_price': forms.TextInput()
        }


class AddSpecifications(ModelForm):
    class Meta:
        model = Specifications
        fields = '__all__'
        widgets = {
            'car': forms.Select(),
            'weight': forms.TextInput(),
            'seats': forms.TextInput(),
            'engine': forms.TextInput()
        }