# Utilizamos la imagen oficial de Python
FROM python:alpine

# Establecemos el directorio de trabajo
WORKDIR /app

# Copiamos el script de Python al directorio de trabajo
COPY script.py .

# Ejecutamos el script de Python
CMD ["python", "script.py"]