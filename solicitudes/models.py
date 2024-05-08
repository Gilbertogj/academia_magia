from django.db import models

# Create your models here.

class SolicitudIngreso(models.Model):
    """
    Modelo para almacenar solicitudes de ingreso de estudiantes.
    """
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    identificacion = models.CharField(max_length=10)
    edad = models.PositiveIntegerField()
    
    # Opciones para afinidad mágica
    AFINIDAD_CHOICES = [
        ('Oscuridad', 'Oscuridad'),
        ('Luz', 'Luz'),
        ('Fuego', 'Fuego'),
        ('Agua', 'Agua'),
        ('Viento', 'Viento'),
        ('Tierra', 'Tierra'),
    ]
    afinidad_magica = models.CharField(max_length=20, choices=AFINIDAD_CHOICES)
    
    # Opciones para el estado de la solicitud
    ESTATUS_CHOICES = [
        ('En revisión', 'En revisión'),
        ('Aprobada', 'Aprobada'),
        ('Rechazada', 'Rechazada'),
    ]
    estatus = models.CharField(max_length=20, choices=ESTATUS_CHOICES, default='En revisión')
    created_at = models.DateTimeField(auto_now_add=True)
    tipo_trebol_grimorio = models.CharField(max_length=20, blank=True)  

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

