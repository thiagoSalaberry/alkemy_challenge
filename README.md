# Ejecución

1. Descargar o clonar este repo ⬇ [alkemy_challenge.rar](alkemy_challenge.rar)
2. Crear un entorno virtual de la siguiente manera
   En tu consola o línea de comandos de bash:

   ## bash

   1️⃣
   python -m venv venv
   source venv/Script/activate

   2️⃣
   pip install -r requirements.txt

   3️⃣
   py index.py

# Proceso

## Extracción

1. Descargaremos los 3 archivos propuestos definiendo una función ƒ download_csv(csv_url: str) -> bytes
2. Los guardaremos de la forma pedida definiendo una función ƒ save_csv(file_path: str, file_name: str, csv_data: bytes) -> None
3. Crearemos una función ƒ read_csv(file_path: str, file_name: str) -> pd.DataFrame que devolverá un DataFrame con información cruda

## Transformación

1. Definiremos las transformaciones que le aplicaremos a los DataFrames mediante funciones, las cuales son:
   - ƒ delete_columns(df: pd.DataFrame, columns_to_keep: list,) -> pd.DataFrame:
   - ƒ define_columns_types(df: pd.DataFrame, columns_types: dict) -> pd.DataFrame:
   - ƒ rename_columns(df: pd.DataFrame, new_columns_names: dict) -> pd.DataFrame:
   - ƒ add_column(df: pd.DataFrame, column_name: str, dtype: type, logic: callable) -> pd.DataFrame:
2. Crearemos una función ƒ complete_transform(df: pd.DataFrame) -> pd.DataFrame que devuelva el DataFrame con todas las transformaciones aplicadas
3. Obtendremos el DataFrame 'normalized' que será la concatenación de los 3 DataFrames de cada una de las entidades
4. Cuando lo tengamos, crearemos una función ƒ combine(df: pd.DataFrame) -> pd.DataFrame que nos devolverá un DataFrame con el total de las entidades agrupadas por categoría y provincia
5. A través de una función ƒ cinemas_df(df: pd.DataFrame) -> pd.DataFrame obtendremos el DataFrame relativo a la información de todos los cines del país

## Carga

1. Crearemos los scripts .sql para la creación de las tablas 'normalized', 'combined', 'cinemas'
2. Crearemos un script .py que se encargue de ejecutar dichos scripts .sql
3. A través de la librería sqlalchemy y mediante el método .to_sql(args) insertaremos los datos en la tabla pertinente. En caso de que ya existan datos, los reemplazaremos
