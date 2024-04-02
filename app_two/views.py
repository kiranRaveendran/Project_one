from django.shortcuts import render, redirect
from . models import *
from .forms import *
# Create your views here.


def home(request):
    return render(request, 'home.html')


def student_Details(request):
    return render(request, 'student_details.html')


def add_student(request):
    v_form = Student_form()
    if request.method == 'POST':
        v_form = Student_form(request.POST, request.FILES)
        if v_form.is_valid():
            v_form.save()
            return redirect('home2')
    else:
        v_form = Student_form()
    context = {'form': v_form}
    return render(request, 'add_student.html', context)
