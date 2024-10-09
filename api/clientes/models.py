from django.db import models

class Cliente(models.Model):
    rut = models.CharField(max_length=12, unique=True)
    nombres = models.CharField(max_length=255)
    apellido_p = models.CharField(max_length=255)
    apellido_m = models.CharField(max_length=255)
    direccion = models.TextField()

    def __str__(self):
        return f'{self.nombres} {self.apellido_p} {self.apellido_m} - {self.rut} - {self.direccion}'
