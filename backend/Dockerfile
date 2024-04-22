# Usamos una imagen de Python como base
FROM python:3.9-slim as base

# Indicamos el directorio de trabajo en el contenedor
WORKDIR /app

# Copiamos los archivos de requerimientos e instalamos las dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Definimos otra etapa para la ejecución de la aplicación
FROM base as app

# Copiamos los archivos de la aplicación al directorio de trabajo
COPY . .

# Exponemos el puerto en el que la aplicación se ejecutará
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]