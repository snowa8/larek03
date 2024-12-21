from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Product, Customer
from .forms import CategoryForm, ProductForm, CustomerForm


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'app/category_list.html', {'categories': categories})


def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'app/category_detail.html', {'category': category})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'app/product_list.html', {'products': products})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'app/product_detail.html', {'product': product})


def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'app/customer_list.html', {'customers': customers})


def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    return render(request, 'app/customer_detail.html', {'customer': customer})


def home(request):
    if request.method == 'GET':
        return render(request, 'app/home.html')
