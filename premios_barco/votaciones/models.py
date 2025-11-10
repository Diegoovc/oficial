from django.db import models

# Create your models here.
from django.db import models

class Respuesta(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    voto = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} - {self.categoria}: {self.voto}"
