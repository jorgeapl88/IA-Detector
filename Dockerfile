# Usamos Python como base
FROM python:3.10-slim

# Creamos una carpeta de trabajo dentro de Docker
WORKDIR /app

# Copiamos el archivo de librerías y las instalamos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos todo el contenido de tu carpeta actual a Docker
COPY . .

# Exponemos el puerto donde corre FastAPI
EXPOSE 8000

# Comando para arrancar tu App
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]