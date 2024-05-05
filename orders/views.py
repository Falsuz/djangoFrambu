from django.shortcuts import render
from .models import Product, Category, Order
import requests 

# Create your views here.
def home(request):
    return render(request, 'index.html', {})

def listProducts(request):
    # mejorar el html para mostrar el producto, nombre y descripcion
    # agregarlos manualmente desde admin y lo mismo para las categorías
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

# def listCategories(request):
#     categories = Category.objects.all()
#     return render(request, 'categories.html', {'categories': categories})

# def listOrders(request):
#     orders = Order.objects.all()
#     return render(request, 'orders.html', {'orders': orders})

# def listOrderbyName(request, name):
#     orders = Order.objects.filter(name=name)
#     if orders.exists():
#         order = orders.first()
#         return render(request, 'dashboard.html', {'order': order})
#     else:
#         return render(request, 'order_not_found.html')

def readApi(request):
    url = 'https://arquiapiframbu.onrender.com/orders'
    
    # Realizar solicitud GET a la URL de la API
    response = requests.get(url)
    
    # Verificar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Convertir la respuesta a JSON
        api_data = response.json()
        
        # Pasar los datos de la API al contexto del renderizado del HTML
        return render(request, 'dashboard.html', {'api_data': api_data})
    else:
        # Si la solicitud no fue exitosa, renderizar un mensaje de error
        return render(request, 'api_error.html')
