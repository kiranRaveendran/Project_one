from django import forms
from .models import *


class Product_Form(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'image', 'price', 'description']

        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control block w-full px-3 py-2 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm border border-gray-300 rounded-md'}),
            'name': forms.TextInput(attrs={'class': 'form-control block w-full px-3 py-2 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm border border-gray-300 rounded-md'}),
            'price': forms.TextInput(attrs={'class': 'form-control block w-full px-3 py-2 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm border border-gray-300 rounded-md'}),
            'description': forms.Textarea(attrs={'class': 'form-control block w-full px-3 py-2 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm border border-gray-300 rounded-md'}),
        }


class School_database_form(forms.ModelForm):
    class Meta:
        model = school_database
        fields = ['name', 'address', 'phone']
