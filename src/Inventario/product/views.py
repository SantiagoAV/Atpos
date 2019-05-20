from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse


from .forms import ProductForm
from .models import product


# Create your views here.
def buscar(request, codigoBarras):
    return HttpResponseRedirect("Detalles del producto %s" %codigoBarras)

def registrar(request):


        form = ProductForm(request.POST or None)
        if form.is_valid():
            form.save()
            form = ProductForm()
        context = {
            'form': form,
        }
        return render(request, 'Post_producto.html', context)



def listarProductos(request):
    queryset = product.objects.all()
    context = {
        'productos_list' : queryset
    }
    return render(request, 'List_producto.html', context)

def index(request):
    return render(request, 'index.html')

