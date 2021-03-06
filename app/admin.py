from django.contrib import admin
from .models import Marca, Producto, Contacto #, ImagenProducto
from .forms import ProductoForm

#-------------------------------------------------
# Validaciones aplicables en admin de django
#-------------------------------------------------
class ProductoAdmin(admin.ModelAdmin):
    form = ProductoForm

# Register your models here.
admin.site.register(Marca)
admin.site.register(Producto)
admin.site.register(Contacto)