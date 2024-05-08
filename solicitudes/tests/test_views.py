

import pytest
import random
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from solicitudes.models import SolicitudIngreso
from solicitudes.serializers import SolicitudIngresoSerializer

@pytest.fixture
def solicitud_ingreso_con_grimorio():
    # Crea una solicitud de ingreso con un tipo de trebol asignado
    solicitud = SolicitudIngreso.objects.create(
        nombre='Juan',
        apellido='Perez',
        identificacion='1234567890',
        edad=25,
        afinidad_magica='Luz',
        estatus='Aprobada',
        tipo_trebol_grimorio='Una hoja'
    )
    return solicitud

@pytest.mark.django_db
def test_list_create_solicitud():
    # Prueba la vista SolicitudListCreateAPIView (ListCreateAPIView)
    url = reverse('solicitud-list-create')
    client = APIClient()

    # Realiza la solicitud GET a la URL para obtener la lista de solicitudes
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK

    # Realiza una solicitud POST para crear una nueva solicitud
    data = {
        'nombre': 'Maria',
        'apellido': 'Gomez',
        'identificacion': '9876543210',
        'edad': 30,
        'afinidad_magica': 'Fuego',
        'estatus': 'En revisión'
    }
    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED

@pytest.mark.django_db
def test_retrieve_update_destroy_solicitud(solicitud_ingreso_con_grimorio):
    # Prueba la vista SolicitudRetrieveUpdateDestroyAPIView (RetrieveUpdateDestroyAPIView)
    url = reverse('solicitud-detail', kwargs={'id': solicitud_ingreso_con_grimorio.id})
    client = APIClient()

    # Realiza la solicitud GET para obtener detalles de la solicitud
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK

    # Realiza la solicitud PATCH para actualizar parcialmente la solicitud
    data = {'estatus': 'Aprobada'}
    response = client.patch(url, data, format='json')
    assert response.status_code == status.HTTP_200_OK

    # Realiza la solicitud DELETE para eliminar la solicitud
    response = client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT

@pytest.mark.django_db
def test_update_status_solicitud(solicitud_ingreso_con_grimorio):
    # Prueba la vista SolicitudUpdateStatusAPIView (UpdateAPIView)
    url = reverse('solicitud-update-status', kwargs={'id': solicitud_ingreso_con_grimorio.id})
    client = APIClient()

    # Realiza la solicitud PATCH para actualizar el estatus de la solicitud
    data = {'estatus': 'Aprobada'}
    response = client.patch(url, data, format='json')
    assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_list_asignaciones(solicitud_ingreso_con_grimorio):
    # Prueba la vista AsignacionesListAPIView (ListAPIView)
    url = reverse('asignaciones-list')
    client = APIClient()

    # Realiza la solicitud GET para obtener la lista de asignaciones de Grimorios
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) > 0