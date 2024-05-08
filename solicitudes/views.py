from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import SolicitudIngreso
from .serializers import SolicitudIngresoSerializer
import random




class SolicitudListCreateAPIView(generics.ListCreateAPIView):
     """
     Vista genérica para listar todas las solicitudes de ingreso o crear una nueva solicitud de ingreso.

     - GET: Devuelve una lista de todas las solicitudes de ingreso existentes.
     - POST: Crea una nueva solicitud de ingreso con los datos proporcionados en el cuerpo de la solicitud.
     """
     queryset = SolicitudIngreso.objects.all()
     serializer_class = SolicitudIngresoSerializer

class SolicitudRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
     """
     Vista genérica para obtener, actualizar o eliminar una solicitud de ingreso específica.

     - GET: Obtiene los detalles de una solicitud de ingreso específica.
     - PUT: Actualiza todos los campos de una solicitud de ingreso.
     - PATCH: Actualiza parcialmente una solicitud de ingreso.
     - DELETE: Elimina una solicitud de ingreso.
     """
     queryset = SolicitudIngreso.objects.all()
     serializer_class = SolicitudIngresoSerializer
     lookup_url_kwarg = 'id'  

class SolicitudUpdateStatusAPIView(generics.UpdateAPIView):
     """
     Vista genérica para actualizar el estatus de una solicitud de ingreso específica.

     - PATCH: Actualiza el estatus de una solicitud de ingreso específica.
     """
     queryset = SolicitudIngreso.objects.all()
     serializer_class = SolicitudIngresoSerializer
     lookup_url_kwarg = 'id'  

     def patch(self, request, *args, **kwargs):
          """
          Actualiza parcialmente el estatus de una solicitud de ingreso específica.

          Se espera recibir el nuevo estatus en el cuerpo de la solicitud.
          """
          instance = self.get_object()
          serializer = self.get_serializer(instance, data=request.data, partial=True)
          serializer.is_valid(raise_exception=True)
          self.perform_update(serializer)
          return Response(serializer.data)

class AsignacionesListAPIView(generics.ListAPIView):
     """
     Vista genérica para listar todas las asignaciones de Grimorios (solicitudes con Grimorios asignados).

     - GET: Devuelve una lista de todas las solicitudes de ingreso con Grimorios asignados.
     """
     queryset = SolicitudIngreso.objects.exclude(tipo_trebol_grimorio__isnull=True)
     serializer_class = SolicitudIngresoSerializer
