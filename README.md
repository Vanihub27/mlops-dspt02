# mlops-dspt02
#  Proyecto Integrador MLOps – Avance 1

## Versionamiento, Estructura y Análisis Exploratorio de Datos

---

##  Descripción del proyecto

Este repositorio corresponde al **Avance 1 del Proyecto Integrador de MLOps (Henry)**, cuyo objetivo principal es establecer una base sólida de trabajo mediante:

* Correcto **versionamiento con Git y GitHub**
* Organización del proyecto bajo una **estructura escalable**
* Configuración de un **entorno virtual reproducible**
* Desarrollo de un **análisis exploratorio de datos (EDA)**

En esta etapa se trabaja con un dataset de ejemplo (no productivo), simulando el flujo inicial de un proyecto de ciencia de datos en un entorno profesional.

---

##  Objetivos del avance

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

##  Carga de datos

El archivo `carga_datos.py` se encarga de:

* Leer el dataset desde un archivo `.csv`
* Realizar una carga inicial en memoria
* Preparar los datos para su análisis posterior

Este enfoque simula una etapa previa al consumo de datos desde un **Data Warehouse o Data Lake**.

---

##  Análisis Exploratorio de Datos (EDA)

El notebook `comprension_eda.ipynb` incluye:

###  Exploración inicial

* Estructura del dataset (`df.info()`)
* Tipos de variables
* Revisión de valores nulos
* Normalización de formatos

###  Análisis univariable

* Variables numéricas:

  * Distribuciones (histogramas)
  * Boxplots
  * Medidas estadísticas (media, mediana, dispersión)
* Variables categóricas:

  * Frecuencias (`value_counts`)
  * Visualización de categorías

###  Análisis bivariable y multivariable

* Relación entre variables
* Correlaciones
* Identificación de patrones
* Primeras hipótesis de comportamiento

---

##  Flujo de trabajo (Git)

Este proyecto sigue un flujo básico de versionamiento:

* Rama base: `main`
* Rama de desarrollo: `developer`
* Desarrollo de features en ramas intermedias
* Integración mediante **Pull Requests**
* Merge final hacia `main`

---

##  Buenas prácticas aplicadas

* ✔ Separación de responsabilidades (script vs notebook)
* ✔ Uso de entorno virtual
* ✔ Gestión de dependencias
* ✔ Versionamiento con ramas
* ✔ Documentación clara
* ✔ Estructura escalable para futuras etapas

---

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

---

## Nota

Este proyecto forma parte de un proceso de formación intensiva en Data Science y MLOps, orientado a la resolución de problemas reales de negocio mediante el uso de datos.

---