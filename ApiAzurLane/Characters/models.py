from django.db import models

# Create your models here.

class Character(models.Model):
    nombre = models.CharField(max_length=250)
    clasificacion = models.CharField(max_length=250)
    faccion = models.CharField(max_length=250)
    imagen = models.ImageField(upload_to='Images')

    def __str__(self):
        return self.nombre