from django.urls import path

from . import views

urlpatterns = [
    path('<int:codigoBarras>/detail/', views.buscar, name='detail'),
    path('productos/', views.listarProductos),
    path('', views.index),
    path('productocreate/', views.registrar),
]