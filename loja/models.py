from django.db import models

# Create your models here.

class Departamentos(models.Model):
    codigo=models.CharField(primary_key=True, max_length=6)
    nomeDepartamento=models.CharField(max_length=50)
    caracteristicas=models.CharField(max_length=100)


    def __str__(self):
     texto = "{0}  {{1}}" 
     return texto.format([self.nomeDepartamento, self.caracteristicas])