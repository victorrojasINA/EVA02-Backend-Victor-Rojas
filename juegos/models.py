from django.db import models

# esto es practicamente como un "molde" o el como se usaran las categorias
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    
    # esto es para que en el panel de admin se vea el nombre y no "objeto (1)"
    def __str__(self):
        return self.nombre

# lo mismo que arriba el "molde" o base para los videojuegos 
class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.IntegerField() 
    stock = models.IntegerField()
    descripcion = models.TextField()

    # aqui conectamos el producto con una categoria
    # on_delete=models.CASCADE significa que si se borra una categoria, sus juegos se borran tambien (sirve para no tener que borrar despues 
    # 1x1 en caso de querer borrar la categoria)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    # para guardar la imagen del juego
    imagen = models.ImageField(upload_to='productos/')

    def __str__(self):
        return self.nombre
    