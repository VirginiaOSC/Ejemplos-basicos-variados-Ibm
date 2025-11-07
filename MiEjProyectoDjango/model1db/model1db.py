from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=64)
    rfc = models.CharField(max_length=15, unique=True)
    fecha_nacimineto = models.DateField()
    activo = models.BooleanField(default=True)

def __str__(self):
        return f"{self.nombre} {self.apellidos}"

class Factura(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    importe = models.DecimalField(max_digits=8,
                    decimal_places=2)
    pagada = models.BooleanField(default=False)
