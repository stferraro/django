# Usa una imagen base de Python
FROM python:3.12

# Establece el directorio de trabajo en el contenedor
WORKDIR /code/inventario

# Copia los archivos de tu proyecto al contenedor
COPY . /code/inventario/

# Instala las dependencias desde el archivo requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expone el puerto 8000 para el servidor de desarrollo de Django
EXPOSE 8000

# Comando para ejecutar la aplicación Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


