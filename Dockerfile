# Usa la imagen base de Python
FROM python:3.9

# Establece la variable de entorno para evitar problemas con la salida estándar de Python
ENV PYTHONUNBUFFERED 1

# Directorio de trabajo en el contenedor
WORKDIR /app
COPY requirements.txt /app/
# Instala las dependencias del sistema (por ejemplo, PostgreSQL client si es necesario)
RUN apt-get update && apt-get install -y postgresql-client
RUN pip install --upgrade pip
# Copia el archivo de requerimientos y lo instala

RUN pip install -r requirements.txt

# Copia todo el código de la aplicación al contenedor
COPY . /app/