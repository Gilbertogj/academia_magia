from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    SolicitudListCreateAPIView,
    SolicitudRetrieveUpdateDestroyAPIView,
    SolicitudUpdateStatusAPIView,
    AsignacionesListAPIView
)


urlpatterns = [
    path('solicitud/', SolicitudListCreateAPIView.as_view(), name='solicitud-list-create'),
    path('solicitud/<int:id>/', SolicitudRetrieveUpdateDestroyAPIView.as_view(), name='solicitud-detail'),
    path('solicitud/<int:id>/estatus/', SolicitudUpdateStatusAPIView.as_view(), name='solicitud-update-status'),
    path('solicitudes/', SolicitudListCreateAPIView.as_view(), name='solicitudes-list'),
    path('asignaciones/', AsignacionesListAPIView.as_view(), name='asignaciones-list'),
    path('solicitud/<int:id>/', SolicitudRetrieveUpdateDestroyAPIView.as_view(), name='solicitud-delete'),
]
