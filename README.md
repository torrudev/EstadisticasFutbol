# 📊 Extractor Estadísticas de Fútbol

Recopila los **máximos goleadores y asistentes** de las cinco grandes ligas europeas (Premier League, La Liga, Serie A, Bundesliga y Ligue 1) en una temporada determinada, y guarda los resultados ordenados en archivos `.csv`.

Esto permite practicar habilidades comunes en proyectos reales de análisis de datos, automatización y consumo de APIs.

## 🎯 Objetivo del Proyecto

Este proyecto tiene fines **educativos** y está diseñado para reforzar conocimientos prácticos de **Python**, enfocados en:

- 🔗 **Conexión con APIs REST**, en este caso con la [API de football-data.org](https://www.football-data.org/).
- 📦 **Manejo de solicitudes HTTP** mediante la biblioteca `requests`.
- 🧹 **Procesamiento de datos JSON** provenientes de una API externa.
- 📄 **Exportación de datos a archivos CSV** para su posterior análisis o almacenamiento.
- 🗂️ **Comprensión de estructuras de proyectos**: Familiarizarse con la organización de carpetas y archivos en proyectos Python, así como las mejores prácticas para **subir únicamente lo necesario a GitHub** (por ejemplo, uso de `.gitignore` y gestión de variables de entorno).

## 🏗 Estructura del proyecto

- **`src/`**: Contiene todo el código fuente del proyecto.
  - **`api/`**: Aquí se maneja la conexión a la API de football-data.org.
  - **`storage/`**: Se encarga de la creación y escritura de los archivos CSV con los resultados.
  - **`main.py`**: El script principal donde se ejecuta la lógica del proyecto.

- **`data/`**: Carpeta que almacena los archivos CSV generados con los resultados.

- **`venv/`**: Entorno virtual que debe ser ignorado por Git, contiene las dependencias instaladas localmente.

- **`.env`**: Archivo utilizado para guardar variables de entorno, como claves de API u otra información sensible.  
  ⚠️ Es importante **no subirlo al repositorio** y asegurarse de que esté incluido en el `.gitignore`.

- **`.gitignore`**: Archivo donde se especifican los archivos y carpetas que Git no debe subir al repositorio (como el entorno virtual, el archivo `.env` o fichero `data/`).

- **`requirements.txt`**: Lista de dependencias del proyecto que pueden ser instaladas con `pip`.

- **`README.md`**: Este archivo, donde se documenta el proyecto.

## ⚙️ Requisitos

- Python 3.13+
- Una cuenta gratuita en [football-data.org](https://www.football-data.org/) para obtener tu clave API

## 🚀 Cómo ejecutar el proyecto

Sigue estos pasos para clonar y poner en marcha el proyecto en tu máquina local:

---

### 1. Clonar el repositorio y navegar hasta él

```bash
git clone https://github.com/torrudev/EstadisticasFutbol.git
cd EstadisticasFutbol
```

### 2. Crear y activar un entorno virtual

Se recomienda trabajar en un **entorno virtual** para aislar las dependencias del proyecto y evitar conflictos con otras instalaciones de Python.

#### En Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

#### En macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar las variables de entorno

Antes de ejecutar el proyecto, es necesario configurar las variables de entorno.

1. Copia el archivo de ejemplo `.env.example` y crea un nuevo archivo `.env`
2. Abre el archivo .env y reemplaza tu_clave_api_aqui por tu API Key real

### 5. Ejecutar main.py

Los archivos CSV se generaran en la carpeta data/

## 🛠️ Herramientas externas recomendadas

A lo largo del proyecto, algunas herramientas externas han sido de gran ayuda:

- [jsonviewer](https://jsonviewer.stack.hu/) — Herramienta utilizada para visualizar y desglosar las respuestas JSON de la API de forma estructurada
