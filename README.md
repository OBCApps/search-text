# Índice Invertido para Búsqueda y Recuperación de Información

Este proyecto se centra en la implementación de un Índice Invertido eficiente para la búsqueda y recuperación de información en documentos de texto. En este README se presentarán los detalles del proyecto, incluyendo los objetivos, la descripción del sistema, los requisitos y las instrucciones de instalación.

## Objetivos

El objetivo principal de este proyecto es desarrollar un sistema de búsqueda y recuperación de información basado en el Índice Invertido. Los objetivos específicos incluyen:

- Implementar el algoritmo de construcción del Índice Invertido.
- Realizar el preprocesamiento de los documentos de texto, incluyendo tokenización y filtrado de stopwords.
- Aplicar el cálculo de pesos TF-IDF para la ponderación de términos.
- Diseñar e implementar una interfaz de usuario para realizar consultas y mostrar los resultados.

## Descripción del Sistema

El sistema se compone de dos partes principales: el backend y el frontend.

### Backend

En el backend, se implementa el Índice Invertido y se realiza el procesamiento de los documentos. Las tareas realizadas incluyen:

- Tokenización: Dividir los documentos en palabras o términos.
- Filtrado de stopwords: Eliminar palabras comunes que no aportan información relevante.
- Cálculo de pesos TF-IDF: Asignar pesos a los términos según su frecuencia en los documentos y en la colección.
- Construcción del Índice Invertido: Estructurar y organizar la información de los términos y documentos.

### Frontend

El frontend consiste en una interfaz de usuario que permite realizar consultas y mostrar los resultados de búsqueda. Las funcionalidades incluyen:

- Entrada de consulta: El usuario puede ingresar una consulta en lenguaje natural.
- Procesamiento de consulta: Se realiza el preprocesamiento de la consulta para buscar los términos relevantes.
- Búsqueda en el Índice Invertido: Se busca en el Índice Invertido los documentos que coincidan con la consulta.
- Presentación de resultados: Los resultados de la búsqueda se muestran al usuario de forma clara y legible.

## Requisitos

Para ejecutar el proyecto, se requiere tener instalado lo siguiente:

- Python 3.x
- Bibliotecas Python: [mencionar las bibliotecas utilizadas, como NLTK, Pandas, etc.]

## Instrucciones de Instalación

1. Clonar el repositorio del proyecto desde GitHub.
2. Crear un entorno virtual en Python:
