from rest_framework import serializers
from .models import SolicitudIngreso
import random

class SolicitudIngresoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolicitudIngreso
        fields = ['id', 'nombre', 'apellido', 'identificacion', 'edad', 'afinidad_magica', 'estatus', 'tipo_trebol_grimorio']
        read_only_fields = ['id', 'tipo_trebol_grimorio','created_at']

    def create(self, validated_data):
        # Crear una nueva instancia de SolicitudIngreso
        solicitud = SolicitudIngreso.objects.create(**validated_data)
        
        # Verificar si la solicitud está aprobada y no tiene Grimorio asignado
        if solicitud.estatus == 'Aprobada' and not solicitud.tipo_trebol_grimorio:
            # Definir probabilidades ponderadas para cada tipo de trébol
            probabilidades = [
                ('Una hoja', 0.4),
                ('Dos hojas', 0.3),
                ('Tres hojas', 0.2),
                ('Cuatro hojas', 0.1),
                ('Cinco hojas', 0.05)
            ]
            
            # Elegir aleatoriamente un tipo de trébol basado en las probabilidades definidas
            tipo_trebol_aleatorio = random.choices(
                [tipo for tipo, prob in probabilidades], 
                weights=[prob for tipo, prob in probabilidades]
            )[0]
            
            # Asignar el tipo de trébol al Grimorio de la solicitud y guardarla
            solicitud.tipo_trebol_grimorio = tipo_trebol_aleatorio
            solicitud.save()

        return solicitud