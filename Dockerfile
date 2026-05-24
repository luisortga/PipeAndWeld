# Utilizamos la imagen oficial de Python
FROM python:alpine

# Establecemos el directorio de trabajo
WORKDIR /src/

# Copiamos el script de Python al directorio de trabajo
COPY main.py .

# Ejecutamos el script de Python
CMD ["python", "main.py"]