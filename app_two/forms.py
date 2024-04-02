from django import forms
from .models import student_doc


class Student_form(forms.ModelForm):
    class Meta:
        model = student_doc
        fields = ['name', 'image', 'student_id', 'address']
        # widgets = {
        #     'image': forms.FileInput(attrs={'class': 'form-control block w-full px-3 py-2 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm border border-gray-300 rounded-md'}),
        #     'name': forms.TextInput(attrs={'class': 'form-control block w-full px-3 py-2 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm border border-gray-300 rounded-md'}),
        #     'student_id': forms.TextInput(attrs={'class': 'form-control block w-full px-3 py-2 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm border border-gray-300 rounded-md'}),
        #     'address': forms.Textarea(attrs={'class': 'form-control block w-full px-3 py-2 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm border border-gray-300 rounded-md'}),
        # }
