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


# Proyecto Integrador MLOps – Avance 2

# 💳 Predicción de Pago de Créditos (Machine Learning)

Este proyecto desarrolla un modelo de **Machine Learning** para predecir si un cliente realizará el pago de su crédito a tiempo.

El trabajo se enmarca dentro de un flujo de análisis y modelado que incluye:
- exploración de datos,
- ingeniería de variables,
- entrenamiento de modelos,
- evaluación comparativa de desempeño.

---

## 🎯 Objetivo

Construir un modelo capaz de clasificar clientes según su probabilidad de **pago a tiempo**, permitiendo anticipar riesgos y mejorar la toma de decisiones en una empresa financiera.

---

## 📁 Estructura del proyecto

```bash
mlops-dspt02/
│
├── src/
│   ├── carga_datos.py
│   ├── comprension_eda.ipynb
│   ├── ft_engineering.py
│   ├── model_training.py
│   ├── model_evaluation.py
│   └── model_training_evaluation.ipynb
│
├── Base_de_datos.xlsx
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🔄 Flujo de trabajo

### 1. 📥 Carga de datos
Se implementa `carga_datos.py` para centralizar la lectura del dataset.  
Permite desacoplar el origen de datos del resto del pipeline.

---

### 2. 🔍 Análisis Exploratorio (EDA)
Se realiza en `comprension_eda.ipynb`.  
Se analizan:
- distribución de variables,
- valores faltantes,
- relaciones con la variable objetivo (`Pago_a_tiempo`).

---

### 3. ⚙️ Feature Engineering
Implementado en `ft_engineering.py`.  
Incluye:
- selección de variables,
- separación en numéricas, categóricas y ordinales,
- construcción de pipelines con `ColumnTransformer`.

---

### 4. 🤖 Entrenamiento de modelos
Implementado en `model_training.py`.  
Se entrenan distintos modelos de clasificación y se aplica validación cruzada para evaluar su desempeño.

---

### 5. 📊 Evaluación de modelos
Implementado en `model_evaluation.py`.  
Se calculan métricas clave:
- Accuracy  
- Precision  
- Recall  
- F1-score  

Se generan comparaciones entre modelos para identificar el mejor desempeño.

---

### 6. 🧪 Experimentación
Notebook: `model_training_evaluation.ipynb`  

Permite:
- probar configuraciones,
- visualizar resultados,
- analizar performance de los modelos.

---

## 📈 Métricas utilizadas

Dado que el problema es de clasificación, se priorizan métricas que permiten evaluar el desempeño del modelo en distintos aspectos:

- **Accuracy**: proporción de predicciones correctas.  
- **Precision**: qué tan precisas son las predicciones positivas.  
- **Recall**: capacidad de detectar correctamente los casos positivos.  
- **F1-score**: balance entre precisión y recall.  

---

## 🧠 Enfoque

El proyecto sigue buenas prácticas de Data Science:

- separación de lógica en módulos (`src/`)
- uso de pipelines para evitar *data leakage*
- evaluación consistente entre modelos
- organización reproducible del flujo de trabajo

---

## 🚀 Próximos pasos

- selección del mejor modelo  
- despliegue en API  
- monitoreo de performance en producción  
- detección de *data drift*  

---

## 🛠 Tecnologías utilizadas

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Jupyter Notebook  

---

## 👩‍💻 Autor

Proyecto desarrollado por **Vanina Cavallin**  
Como parte del programa de formación en Data Science.