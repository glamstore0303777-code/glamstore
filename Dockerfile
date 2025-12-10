FROM python:3.11-slim

WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements
COPY requirements.txt .

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código de la aplicación
COPY . .

# Crear directorio para archivos estáticos
RUN mkdir -p /app/staticfiles

# Exponer puerto
EXPOSE 8000

# Comando de inicio
CMD ["gunicorn", "glamstore.wsgi:application", "--bind", "0.0.0.0:8000"]
