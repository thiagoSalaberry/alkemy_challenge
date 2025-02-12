# Challenge Data Analytics - Python 🚀

## Objetivo 🎯

Crear un proyecto en Python que consuma datos desde tres fuentes distintas para popular una base de datos SQL con información cultural sobre bibliotecas, museos y salas de cine argentinos.

## Requerimientos funcionales ⚙

El proyecto deberá cumplir con una serie de requerimientos funcionales que giran en torno a cuetro ejes centrales: los archivos fuente, el procesamiento de datos, la creación de tablas en la base de datosy la actualización de la base de datos.

### Archivos fuente 📃

Los archivos fuentes serán utilizados en el proyecto para obtener de ellos todo lo necesario para popular la base de datos. El proyecto deberá:

- Obtener los 3 archivos de fuente utilizando la librería requests y almacernarse en forma local (tener en cuenta que las URLs pueden cambiar a futuro):

  - Datos Argentina - Museos
  - Datos Argentina - Salas de cine
  - Datos Argentina - Bibliotecas Populares

- Organizar los archivos en rutas siguiendo la siguiente estructura: "categoria/año-mes/categoria-dia-año-mes.csv"
  - Por ejemplo: "museos/2021-noviembre/museos-03-11-2021"
  - Si el archivo existe debe reemplazarse. La fecha de la nomenclatura es la fecha de descarga

## Procesamiento de datos 🛠

El procesamiento de datos permitirá a nuestro proyecto transformar los datos de los archivos fuente en la información que va a nutrir la base de datos. Para esto, el proyecto deberá:

- Normalizar toda la información de Museos, Salas de Cine y Bibliotecas Populares, para crear una única tabla que contenga:

1. cod_localidad
2. id_provincia
3. id_departamento
4. categoria
5. provincia
6. localidad
7. nombre
8. domicilio
9. codigo_postal
10. numero_de_telefono
11. mail
12. web

- Procesar los datos conjuntos para generar una tabla con la siguiente información:

1. Cantidad de registros totales por categoría
2. Cantidad de registros totales por fuente
3. Cantidad de registros por provincia y categoría

- Procesar la información de cines para poedr crear una tabla ue contenga:

1. Provincia
2. Cantidad de pantallas
3. Cantidad de butacas
4. Cantidad de espacios INCAA

## Creación de tablas en la base de datos 📅

Para disponibilizar la información obtenida y procesada en los pasos previos, el proyecto deberá tener una base de datos que cumpla con los siguiente requisitos:

- La base de datos debe ser PostgreSQL
- Se deben crear los scripts .sql para la creación de las tablas
- Se debe crear un script .py ue ejecute los scripts .sl para facilitar el deploy
- Los datos de la conexión deben poder configurarse fácilmente para facilitar el deploy en un nuevo ambiente si es necesario

## Actualización de la base de datos 🔄

Luego de normalizar la información y generar las demás tablas, las mismas deben actualizar la base de datos. Para eso,es importante tener en cuenta:

- Todos los registros existentes deben ser reemplazados por la nueva información
- Dentro de cada tabla debe indicarse en una columna adicionalla fecha de carga
- Los registros para los cuales la fuente no brinda información deben cargarse como nulos

## Requerimientos técnicos 🔧

La aplicación deberá cumplir con una serie de requerimientos técnicos que giran en torno a 7 ejes centrales.

### Ejecución ▶

La descarga, procesamiento y actualización de la información de la base de datos se debe poder ejecutar desde un archivo .py.

### Deploy 🚚

El proyecto debe poder deployarse de forma sencilla siguiendo un README, que al menos contenga las instrucciones para:

- Utilizarse creando un entorno virtual (venv)
- Instalar las dependencias necesarias con pip
- Configurar la conexión a la base de datos

### Configuración ⚙

Las configuraciones necesarias para que el proyecto se ejecute deben pode configurarse desde un archivo .env, .ini o similar con la librería python-decouple.

### Logs 💻

El programa debe crear logs oportunos sobre la ejecución del mismo con la librería logging.

### Base de datos 💾

Se deben dejar disponibles los scripts de creación de las tablas utilizadas.

### Conexión a la base de datos 🔌

- Los datos se deben almacenar en una base de datos PostgreSQL
- La conexión a la base de datos se debe implementar con la librería y ORM SQLalchemy
- Se recomienda ver la funcionalidad de pandas dataframe.to_sql

### Herramientas para el procesamiento de datos ⚒

Utilizar la librería Pandas para procesar todos los datos que sean necesarios

## Criteríos a evaluar ✅

A la hora del evaluar el challenge, se tendrá en cuenta una serie de criterios que permitirán medir en detalle el producto alcanzado. Estos son:

- Implementación de buenas prácticas de codificación y estilo de código (segun PEP8)
- Comentarios oportunos y docstrings descriptivos
- Manejo de excepciones preciso, no azaroso
- La estructura del proyecto debe ser limpia y ordenada
- El código deberá estar modularizado en componentes reutilizables e independientes.
