from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('productos/<pk>/', views.darProducto, name='detail'),
    path('productos/', views.listarProductos),
    path('', views.index),
    path('productocreate/', views.registrar),
]