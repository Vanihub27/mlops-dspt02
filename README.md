# mlops-dspt02

# Proyecto Integrador MLOps – Avance 1

## Versionamiento, Estructura y Análisis Exploratorio de Datos

---

## Descripción del proyecto

Este repositorio corresponde al **Avance 1 del Proyecto Integrador de MLOps (Henry)**, cuyo objetivo principal es establecer una base sólida de trabajo mediante:

* Correcto **versionamiento con Git y GitHub**
* Organización del proyecto bajo una **estructura escalable**
* Configuración de un **entorno virtual reproducible**
* Desarrollo de un **análisis exploratorio de datos (EDA)**

En esta etapa se trabaja con un dataset de ejemplo (no productivo), simulando el flujo inicial de un proyecto de ciencia de datos en un entorno profesional.

---

## Objetivos del avance

* Implementar buenas prácticas de **control de versiones**
* Establecer una **estructura clara de proyecto**
* Crear un entorno reproducible con `requirements.txt`
* Realizar una **exploración inicial de los datos**
* Identificar:

  * Tipos de variables
  * Valores nulos
  * Posibles inconsistencias
  * Primeras hipótesis analíticas

---

## Estructura del repositorio
##  Estructura del repositorio

```
mlops-dspt02/
│
├── src/
│   ├── carga_datos.py              # Script para carga del dataset
│   └── comprension_eda.ipynb       # Análisis exploratorio de datos (EDA)
│
├── requirements.txt                # Dependencias del proyecto
├── README.md                       # Documentación del proyecto
└── .gitignore                      # Archivos ignorados por Git
```

---

## Configuración del entorno
##  Configuración del entorno

### 1. Clonar el repositorio

```bash
git clone https://github.com/Vanihub27/mlops-dspt02.git
cd mlops-dspt02
```

### 2. Crear entorno virtual

```bash
python -m venv venv
```

### 3. Activar entorno virtual

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / Mac:**

```bash
source venv/bin/activate
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Carga de datos
##  Carga de datos

El archivo `carga_datos.py` se encarga de:

* Leer el dataset desde un archivo `.csv`
* Realizar una carga inicial en memoria
* Preparar los datos para su análisis posterior

Este enfoque simula una etapa previa al consumo de datos desde un **Data Warehouse o Data Lake**.

---

## Análisis Exploratorio de Datos (EDA)

El notebook `comprension_eda.ipynb` incluye:

### Exploración inicial
##  Análisis Exploratorio de Datos (EDA)

El notebook `comprension_eda.ipynb` incluye:

###  Exploración inicial

* Estructura del dataset (`df.info()`)
* Tipos de variables
* Revisión de valores nulos
* Normalización de formatos

### Análisis univariable
###  Análisis univariable

* Variables numéricas:

  * Distribuciones (histogramas)
  * Boxplots
  * Medidas estadísticas (media, mediana, dispersión)
* Variables categóricas:

  * Frecuencias (`value_counts`)
  * Visualización de categorías

### Análisis bivariable y multivariable
###  Análisis bivariable y multivariable

* Relación entre variables
* Correlaciones
* Identificación de patrones
* Primeras hipótesis de comportamiento

---

## Flujo de trabajo (Git)
##  Flujo de trabajo (Git)

Este proyecto sigue un flujo básico de versionamiento:

* Rama base: `main`
* Rama de desarrollo: `developer`
* Desarrollo de features en ramas intermedias
* Integración mediante **Pull Requests**
* Merge final hacia `main`

---

## Buenas prácticas aplicadas
##  Buenas prácticas aplicadas

* ✔ Separación de responsabilidades (script vs notebook)
* ✔ Uso de entorno virtual
* ✔ Gestión de dependencias
* ✔ Versionamiento con ramas
* ✔ Documentación clara
* ✔ Estructura escalable para futuras etapas

---

## Autora
##   Próximos pasos

En los siguientes avances se abordará:

* Ingeniería de features
* Modelado predictivo
* Validación de modelos
* Pipeline de Machine Learning
* Implementación de prácticas MLOps

---

##   Autora

**Vanina Cavallin**
Dra. en Ciencias Biológicas | Data Scientist en formación

    [GitHub](https://github.com/Vanihub27)
  [GitHub](https://github.com/Vanihub27)

---

## Nota

Este proyecto forma parte de un proceso de formación intensiva en Data Science y MLOps, orientado a la resolución de problemas reales de negocio mediante el uso de datos.

---
# 🚀 Proyecto de Modelado Predictivo de Créditos

Este repositorio contiene el desarrollo de un **modelo de machine learning** para predecir el comportamiento de nuevos clientes en una empresa financiera.  
El proyecto se enmarca dentro de un flujo **MLOps**, garantizando buenas prácticas de colaboración, pruebas, despliegue y monitoreo.

---

# 📊 Proyecto de Modelado Predictivo de Créditos

Este repositorio contiene el desarrollo de un **modelo de machine learning** para predecir el comportamiento de nuevos u
en una empresa financiera.

El proyecto se enmarca dentro de un flujo **MLOps**, garantizando buenas prácticas de colaboración, pruebas, despliegue y monitoreo.

---

# Proyecto Integrador MLOps – Avance 3

## 📁 Estructura del proyecto

```bash
mlops_pipeline/
│
├── src/
│   ├── Cargar_datos.ipynb
│   ├── comprension_eda.ipynb
│   ├── ft_engineering.py
│   ├── heuristic_model.py
│   ├── model_training.py
│   ├── model_deploy.py
│   ├── model_evaluation.py
│   └── model_monitoring.py
│
├── Base_de_datos.csv
├── requirements.txt
├── .gitignore
├── readme.md
└── set_up.bat
```

---

## 🚀 Flujo de trabajo

1. **Cargar_datos.ipynb**  
Notebook para cargar datos desde un CSV de ejemplo.  
> *En producción, Los datos se cargarán desde DWH o Data Lake.*

2. **comprension_eda.ipynb**  
Análisis exploratorio de datos (EDA) y generación de artefactos experimentales.

3. **ft_engineering.py**  
Creación de *features* y división de datos en entrenamiento y validación.  
Incluye construcción de pipelines.

4. **heuristic_model.py**  
Modelo base de referencia (benchmark heurístico).

5. **model_training.py**  
Entrenamiento y evaluación de múltiples modelos.  
- Funciones clave: `sumarize_classification` y `build_model`.  
- Incluye tablas comparativas y visualizaciones.

6. **model_deploy.py**  
Despliegue del mejor modelo seleccionado.  
- Creación de una imagen con dependencias y código.  
- Exposición de un **endpoint** para predicciones batch.

7. **model_evaluation.py**  
Generación de métricas del modelo desplegado en un dashboard de evaluación.

8. **model_monitoring.py**  
Monitoreo periódico para:  
- Detectar *data drift*.  
- Comparar predicciones vs. datos reales.  
- Asegurar el desempeño continuo del modelo.

---

## 🚀 Despliegue y Ejecución del Modelo con Docker

Una vez clonado el repositorio se puede levantar el servicio en docker

### 📋 Prerrequisitos

- **Docker Desktop**: Asegúrate de que Docker esté instalado y en ejecución en tu máquina. Puedes descargarlo desde [el sitio oficial de Docker](https://www.docker.com/products/docker-desktop/).
- **Git**: Necesitas Git para clonar este repositorio.
- **Terminal de Comandos**: Una terminal como PowerShell, CMD, Bash, o similar.

### 🛠 Construcción de imagen con docker

En la terminal ejecutar docker build -t api-creditos .

Una vez construida la imagen, este comando la ejecutará como un contenedor:

docker run -d -p 8000:8000 --name api-creditos-container api-creditos