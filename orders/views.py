from django.shortcuts import render
from .models import Product, Category, Order
import requests 

# Create your views here.
def home(request):
    return render(request, 'index.html', {})

def listProducts(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def listCategories(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})

def listOrders(request):
    orders = Order.objects.all()
    return render(request, 'orders.html', {'orders': orders})


