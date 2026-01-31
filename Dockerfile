FROM python:3.9-slim

# Configuración del directorio de trabajo
WORKDIR /app

# Instalación de dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia de archivos y ejecución de pruebas y servidor
COPY . .
CMD sh -c "pytest test_app.py && python app.py"