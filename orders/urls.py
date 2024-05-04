from django.urls import path
from . import views
# url hijo

urlpatterns = [
    path('', views.home, name='home'),
    path('products', views.listProducts, name='products'),
    # path('categories', views.listCategories, name='categories'),
    path('dash',views.readApi, name='dash')
]