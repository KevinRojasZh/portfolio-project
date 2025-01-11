from django.db import models
from django.contrib.auth.models import User


# Modelo para Lenguajes
class Lenguajes(models.Model):
    nombre = models.CharField(
                    verbose_name= 'lenguajes',
                    max_length=100
    )
    
    def __str__(self):
        return self.nombre
    

# Modelo para Developer
class Developer(models.Model):

    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=300)
    ciudad = models.CharField(max_length=100, null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField()
    descripcion = models.TextField()
    tecnologias = models.ManyToManyField("Lenguajes",
                                            verbose_name="tecnologias",
                                            )
    fotos = models.ImageField(upload_to='portafolio/static/', height_field=None, width_field=None, max_length=None)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)




    def __str__(self):
        return self.nombre