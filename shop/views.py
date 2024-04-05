from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *

# Create your views here.
def product_list(request, categoria_id=None):
    categoria = None
    productos = Producto.objects.all()
    if categoria_id:
        categoria = Categoria.objects.get(pk=categoria_id)
        productos = productos.filter(categoria=categoria)
    return render(request, 'product_list.html', {'categoria': categoria, 'productos': productos})

def product_detail(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    return render(request, 'product_detail.html', {'producto': producto})
