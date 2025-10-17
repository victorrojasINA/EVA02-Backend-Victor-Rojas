from django.urls import path
from . import views

# aqui definimos las direcciones/urls
urlpatterns = [
    path('', views.home, name='home'),
    path('categoria/<int:categoria_id>/', views.productos_por_categoria, name='productos_por_categoria'),
    path('producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
]