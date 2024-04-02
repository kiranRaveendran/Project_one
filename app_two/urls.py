from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home2'),
    path('add_student/', views.add_student, name='add_student'),
    path('student_Details/', views.student_Details, name='student_Details'),
    path('update_student/', views.update_student, name='update_student'),
    path('delete_student/<int:pk>/', views.delete_student, name='delete_student'),
    path('student/<int:pk>/', views.student, name='student')
]
