from django.contrib import admin
from .models import Categoria, Producto

# una clase para que la lista de productos en el admin se vea con columnas
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'stock')

# aqui registramos nuestros modelos para que aparezcan en el panel
admin.site.register(Categoria)
admin.site.register(Producto, ProductoAdmin)