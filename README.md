README - Proyecto de Academia de Magia

Este repositorio contiene un proyecto para una academia de magia. 
El proyecto utiliza Docker para facilitar el despliegue y la gestión del entorno de desarrollo. 
A continuación se detallan los pasos para configurar y ejecutar el proyecto localmente.

Requisitos Previos
Tener instalados los siguientes componentes en tu sistema:

Docker: Para crear, gestionar y ejecutar contenedores de aplicaciones.

Docker Compose: Para definir y ejecutar aplicaciones Docker multi-contenedor.

Configuración y Ejecución del Proyecto

1. Clonar el RepositorioClona este repositorio en tu máquina local:

   https://github.com/Gilbertogj/academia_magia.git


2. Configurar Variables de EntornoCrea un archivo .env en el directorio raíz del proyecto y configura las variables de entorno necesarias.

    Asegúrarse de configurar las variables requeridas para la base de datos y otros componentes del proyecto.

3. Ejecutar Docker ComposeLevanta los servicios del proyecto utilizando Docker Compose,
   
4. Este comando construirá las imágenes Docker y ejecutará los contenedores definidos en docker-compose.yml:

      docker-compose up --build

5. Aplicar Migraciones de la Base de DatosAbre una nueva terminal y ejecuta el siguiente comando para aplicar las migraciones de Django:

      docker-compose exec web python manage.py migrate


Acceder a la Aplicación

Una vez que los contenedores estén en ejecución, podrás acceder a la aplicación a través del navegador web:
URL de la Aplicación: http://localhost:8000/
Documentación con Swagger

La documentación de la API está disponible utilizando Swagger. Puedes acceder a la documentación a través de las siguientes URLs:
Swagger UI: http://localhost:8000/docs/
ReDoc: http://localhost:8000/redocs/

Utilización de Django Rest Framework

Este proyecto utiliza Django Rest Framework (DRF) para el desarrollo de la API REST.
DRF proporciona herramientas poderosas para crear APIs web de forma rápida y consistente.


Detener y Limpiar los Contenedores
Para detener y eliminar los contenedores Docker, utiliza el siguiente comando:

docker-compose down

Notas Adicionales

Base de Datos en Docker: La base de datos PostgreSQL está configurada para ejecutarse dentro de un contenedor Docker (db) junto con la aplicación web.


Problemas Comunes y Soluciones
En caso de encontrarte con problemas durante la configuración o ejecución del proyecto, consulta la documentación oficial de 
Django https://docs.djangoproject.com/en/5.0/
y Django Rest Framework https://www.django-rest-framework.org/
También puedes comunicarte con el equipo de desarrollo para obtener asistencia adicional.

