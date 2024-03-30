from django.shortcuts import render, redirect
from . models import Product
from .forms import Product_Form
# Create your views here.


def display(request):
    product = Product.objects.all()
    context = {
        'products': product
    }
    return render(request, 'products.html', context)


def product_Details(request, pk):
    product = Product.objects.get(id=pk)
    context = {
        'products': product
    }
    print(product)
    return render(request, 'product_details.html', context)


def add_Products(request):
    form_variable = Product_Form()
    if request.method == 'POST':
        form_variable = Product_Form(request.POST, request.FILES)
        if form_variable.is_valid():
            form_variable.save()
            return redirect('home')
    else:
        form_variable = Product_Form()
    context = {
        'form': form_variable
    }
    return render(request, 'add_product.html', context)


def update_Product(request, pk):
    pro = Product.objects.get(id=pk)
    form_v = Product_Form(instance=pro)
    if request.method == 'POST':
        form_v = Product_Form(request.POST,  instance=pro)
        if form_v.is_valid():
            form_v.save()
            return redirect('home')
    context = {
        'update': form_v
    }
    return render(request, 'update_product.html', context)
# what is named parameter
# click event
# ankar tag
# pk-primary key
# param'


def deleteProduct(request, pk):
    products = Product.objects.get(id=pk)
    products.delete()
    return redirect('home')
