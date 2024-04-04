from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Tag)
admin.site.register(Producto)
admin.site.register(DetalleCompra)

class ProductoInline(admin.TabularInline):
    model = Producto
    extra = 0
    readonly_fields = ['nombre', 'descripcion', 'precio', 'cantidad_disponible', 'tag']

class CategoriaInline(admin.TabularInline):
    model = Categoria
    extra = 0

class DetalleCompraInline(admin.TabularInline):
    model = DetalleCompra
    extra = 0

class CarritoInline(admin.TabularInline):
    model = Carrito
    extra = 0

class CompraInline(admin.TabularInline):
    model = Compra
    extra = 0

class CategoriaAdmin(admin.ModelAdmin):
    inlines = [CategoriaInline, ProductoInline]
    list_display = ['nombre', 'padre']

class CarritoAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'lista_productos']
    list_filter = ['usuario']
    search_fields = ['usuario__username', 'producto__nombre']

    def lista_productos(self, obj):
        return ", ".join([producto.nombre for producto in obj.productos.all()])  # Obtener los nombres de los productos en el carrito


class CompraAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'fecha_compra', 'precio_total']
    list_filter = ['usuario']
    search_fields = ['usuario__username']
    inlines = [DetalleCompraInline]

admin.site.register(Carrito, CarritoAdmin)
admin.site.register(Compra, CompraAdmin)
admin.site.register(Categoria, CategoriaAdmin)