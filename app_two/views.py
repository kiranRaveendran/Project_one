from django.shortcuts import render, redirect
from . models import *
from .forms import *
# Create your views here.


def home(request):
    return render(request, 'home.html')


def student_Details(request):
    data = student_doc.objects.all()
    context = {'data': data}
    return render(request, 'student_details.html', context)


def student(request, pk):
    student_dl = student_doc.objects.get(pk=pk)
    print(student_dl)
    context = {'student_dl': student_dl}
    return render(request, 'student.html', context)


def add_student(request):
    v_form = Student_form()
    if request.method == 'POST':
        v_form = Student_form(request.POST, request.FILES)
        if v_form.is_valid():
            v_form.save()
            return redirect('student_Details')
    else:
        v_form = Student_form()
    context = {'form': v_form}
    return render(request, 'add_student.html', context)


def update_student(request):
    return


def delete_student(request, pk):
    data = student_doc.objects.get(pk=pk)
    data.delete()
    return redirect('student_Details')
