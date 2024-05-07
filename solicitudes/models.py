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

    # def save(self, *args, **kwargs):
    #     # Asignación automática de Grimorio si la solicitud está aprobada y no tiene Grimorio asignado
    #     if self.estatus == 'Aprobada' and not self.tipo_trebol_grimorio:
    #         # Definir probabilidades ponderadas para cada tipo de trébol
    #         probabilidades = [
    #             ('Una hoja', 0.4),    # Probabilidad alta (común)
    #             ('Dos hojas', 0.3),   # Probabilidad media
    #             ('Tres hojas', 0.2),  # Probabilidad baja
    #             ('Cuatro hojas', 0.1), # Probabilidad muy baja (inusual)
    #             ('Cinco hojas', 0.05)  # Probabilidad mínima (muy raro)
    #         ]
            
    #         # Elegir aleatoriamente un tipo de trébol basado en las probabilidades definidas
    #         tipo_trebol_aleatorio = random.choices(
    #             [tipo for tipo, prob in probabilidades], 
    #             weights=[prob for tipo, prob in probabilidades]
    #         )[0]
            
    #         self.tipo_trebol_grimorio = tipo_trebol_aleatorio

    #     super().save(*args, **kwargs)


# class Grimorio(models.Model):
#     """
#     Modelo para representar grimorios asociados a estudiantes.
#     """
#     TIPO_TREBOL_CHOICES = [
#         ('Una hoja', 'Una hoja'),
#         ('Dos hojas', 'Dos hojas'),
#         ('Tres hojas', 'Tres hojas'),
#         ('Cuatro hojas', 'Cuatro hojas'),
#         ('Cinco hojas', 'Cinco hojas'),
#     ]
#     tipo_trebol = models.CharField(max_length=20, choices=TIPO_TREBOL_CHOICES)

#     #Relaciones
#     estudiante = models.OneToOneField(SolicitudIngreso, on_delete=models.CASCADE, related_name='grimorio')


#     def __str__(self):
#         """
#         Devuelve una representación legible del objeto Grimorio.
#         """
#         return f"Grimorio - {self.tipo_trebol} - Estudiante: {self.estudiante.nombre} {self.estudiante.apellido}"