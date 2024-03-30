from django.urls import path
from . import views

urlpatterns = [
    path('', views.display, name='home'),
    path('pinfo/<int:pk>/', views.product_Details, name='product_details'),
    path('add_product/', views.add_Products, name='add_Products'),
    path('update_product/<int:pk>/',views.update_Product, name='update_product'),
    path('delete/<int:pk>/', views.deleteProduct, name='delete')
]
