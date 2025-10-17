from django.shortcuts import render
from .models import Producto, Categoria

# esta funcion es para la pagina de inicio
def home(request):
    # pedimos todos los productos y categorias a la base de datos
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()

    contexto = {
        'productos': productos,
        'categorias': categorias,
    }
    return render(request, 'juegos/home.html', contexto)

# esta es para cuando haces clic en una categoria
def productos_por_categoria(request, categoria_id):
    # primero encontramos el objeto de la categoria especifica
    categoria = Categoria.objects.get(id=categoria_id)
    # y luego filtramos los productos que pertenecen a esa categoria
    productos_filtrados = Producto.objects.filter(categoria=categoria)
    categorias = Categoria.objects.all()
    contexto = {
        'productos': productos_filtrados,
        'categorias': categorias,
        'categoria_actual': categoria,
    }
    return render(request, 'juegos/home.html', contexto)

# esta es para ver el detalle de un solo juego
def detalle_producto(request, producto_id):
    # buscamos un solo producto por su id
    producto_unico = Producto.objects.get(id=producto_id)
    categorias = Categoria.objects.all()
    contexto = {
        'producto': producto_unico,
        'categorias': categorias, # aqui pasamos las categorias al menu
    }
    return render(request, 'juegos/detalle_producto.html', contexto)