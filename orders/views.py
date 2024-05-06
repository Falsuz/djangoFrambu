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

# def listOrders(request):
#     orders = Order.objects.all()
#     return render(request, 'orders.html', {'orders': orders})

# def name():
#     pass

from django.shortcuts import render, redirect, get_object_or_404
from .models import Order
from .forms import OrderForm

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})

def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'order_detail.html', {'order': order})

def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            return redirect('order_detail', pk=order.pk)
    else:
        form = OrderForm()
    return render(request, 'order_form.html', {'form': form})

def order_update(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            order = form.save()
            return redirect('order_detail', pk=order.pk)
    else:
        form = OrderForm(instance=order)
    return render(request, 'order_form.html', {'form': form})

def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('order_list')
    return render(request, 'order_confirm_delete.html', {'order': order})
