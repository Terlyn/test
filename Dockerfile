# Usa una imagen base de Python compatible con Docker 17.03.1-c
FROM python:3.6-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo de requerimientos en el contenedor
COPY requirements.txt requirements.txt

# Instala las dependencias
RUN pip install -r requirements.txt

# Copia el contenido del proyecto en el contenedor
COPY . .

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
