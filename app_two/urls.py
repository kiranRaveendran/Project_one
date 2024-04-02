from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home2'),
    path('add_student/', views.add_student, name='add_student'),
    path('student_Details/', views.student_Details, name='student_Details')
]
