# Servidor CRUD de Productos - QA Challenge
Este proyecto consiste en una API REST automatizada para la gestión de productos. La solución está diseñada para ejecutarse en un entorno Linux virtualizado mediante contenedores, garantizando que el servidor solo se inicie si las pruebas de calidad previas son exitosas.

## Requisitos Previos
Para ejecutar este proyecto, es indispensable contar con las siguientes herramientas instaladas y ejecutándose:

*   **Docker Desktop**: Motor que permite la creación del entorno virtualizado.
    *   [Descargar Docker para Windows](https://www.docker.com/products/docker-desktop/)
    *   [Descargar Docker para Mac](https://docs.docker.com/desktop/install/mac-install/)
*   **Git**: Herramienta necesaria para la gestión del repositorio.
    *   [Descargar Git](https://git-scm.com/downloads)

## Instrucciones de Ejecución
Siga estos pasos de forma secuencial para poner en marcha el sistema:

### 1. Obtener el código
Abra una terminal (CMD, PowerShell o Terminal de Linux) y clone el repositorio:
```bash
git clone https://github.com/yiNgs71/qa-server.git
cd qa-server
```

### 2. Desplegar la solución
Ejecute el siguiente comando. Este proceso automatiza la configuración del sistema operativo, la instalación de dependencias y la validación de pruebas:
```bash
docker-compose up --build
```

### 3. Resultados esperados
Al ejecutar el comando, la terminal mostrará el siguiente flujo:
*   **Construcción del contenedor**: Configuración del entorno basado en Linux.
*   **Ejecución de Tests**: Se activará la suite de **pytest**. Los puntos verdes indican que el código ha superado las pruebas de integridad.
*   **Inicio del Servidor**: Tras la aprobación de los tests, se habilitará el servidor en el puerto **5000**.


## Acceso al Servicio
Con el servidor activo, puede interactuar con la API mediante la siguiente dirección:
*   **Listado de productos**: [http://localhost:5000/productos](http://localhost:5000/productos)

> **Nota**: El sistema incluye una base de datos **SQLite** con carga automática de datos iniciales (Laptop, Monitor y Licencias) para facilitar su revisión inmediata.


## Estrategia de Pruebas Automatizadas (QA)
Como parte fundamental del rol de QA, el proyecto integra una suite de pruebas que valida los puntos críticos del sistema antes de cada despliegue:
*   **Integridad de Datos**: Verificación de la estructura y disponibilidad de la información.
*   **Funcionalidad CRUD**: Validación de procesos de creación y eliminación dinámica de registros.
*   **Manejo de Errores**: Confirmación de respuestas **HTTP 404** ante solicitudes de recursos inexistentes.
*   **Aislamiento de Entorno**: Uso de bases de datos en memoria para pruebas, evitando la contaminación de los datos de producción.