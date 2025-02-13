"""
En este archivo crearé las funciones necesarias para:
1. Normalizar los datos de cada una de las entidades y obtener una sola tabla con:
    - cod_localidad
    - id_provincia
    - id_departamento
    - categoria
    - provincia
    - localidad
    - nombre
    - domicilio
    - codigo_postal
    - numero_de_telefono
    - mail
    - web
2. Procesar los datos conjuntos para poder generar una tabla con la siguiente info:
    - Cantidad de registros totales por categoría
    - Cantidad de registros totales por fuente
    - Cantidad de registros por provincia y categoría
3. Procesar la información de cines para poder crear una tabla que contenga:
    - Provincia
    - Cantidad de pantallas
    - Cantidad de butacas
    - Cantidad de espacios INCAA
"""
import pandas as pd


def read_csv(file_path: str, file_name: str) -> pd.DataFrame:
    """Lee un archivo CSV y devuelve un DataFrame con los datos del archivo."""
    try:
        return pd.read_csv(f"{file_path}/{file_name}")
    except FileNotFoundError as e:
        print(
            f"Error al leer el archivo {file_name}: {str(e)}")


def delete_columns(df: pd.DataFrame, columns_to_keep: list,) -> pd.DataFrame:
    df = df[columns_to_keep]
    return df


def define_columns_types(df: pd.DataFrame, columns_types: dict) -> pd.DataFrame:
    for column, column_type in columns_types.items():
        if column in df.columns:
            try:
                df[column] = df[column].astype(column_type)
                if column_type == "string":
                    df[column] = df[column].astype("string")
            except Exception as e:
                print(
                    f"❌ Error al convertir la columna {column} al tipo {column_type}: {e}")
    return df


def rename_columns(df: pd.DataFrame, new_columns_names: dict) -> pd.DataFrame:
    df = df.rename(columns=new_columns_names)
    return df


def add_column(df: pd.DataFrame, column_name: str, dtype: type, logic: callable) -> pd.DataFrame:
    if df is None:
        print("DataFrame inválido")
        return
    if column_name not in df.columns:
        df[column_name] = None
        return df

    df[column_name] = df.apply(logic, axis=1).astype(dtype)
    return df


columns = {
    "cines": {
        "from_csv": ['cod_localidad', 'id_provincia', 'id_departamento', 'categoria',
                     'provincia', 'departamento', 'localidad', 'nombre', 'direccion', 'piso',
                     'cp', 'web', 'latitud', 'longitud', 'tipo_latitud_longitud', 'fuente',
                     'sector', 'pantallas', 'butacas', 'tipo_de_gestion', 'espacio_incaa',
                     'año_actualizacion'],
        "to_keep": ['cod_localidad', 'id_provincia', 'id_departamento', 'categoria',
                    'provincia', 'localidad', 'nombre', 'direccion',
                    'cp', 'web'],
        "renamed": {
            "cod_localidad": "cod_localidad",
            "id_provincia": "id_provincia",
            "id_departamento": "id_departamento",
            "categoria": "categoria",
            "provincia": "provincia",
            "localidad": "localidad",
            "nombre": "nombre",
            "direccion": "domicilio",
            "cp": "codigo_postal",
            "web": "web",
        },
        "to_add": ["mail", "cod_area", "numero_de_telefono"]
    },
    "museos": {
        "from_csv": ['Cod_Loc', 'IdProvincia', 'IdDepartamento', 'Observaciones',
                     'categoria', 'subcategoria', 'provincia', 'localidad', 'nombre',
                     'direccion', 'piso', 'CP', 'cod_area', 'telefono', 'Mail', 'Web',
                     'Latitud', 'Longitud', 'TipoLatitudLongitud', 'Info_adicional',
                     'fuente', 'jurisdiccion', 'año_inauguracion', 'actualizacion'],
        "to_keep": ['Cod_Loc', 'IdProvincia', 'IdDepartamento',
                    'categoria', 'provincia', 'localidad', 'nombre',
                    'direccion', 'CP', 'cod_area', 'telefono', 'Mail', 'Web',
                    ],
        "renamed": {
            "Cod_Loc": "cod_localidad",
            "IdProvincia": "id_provincia",
            "IdDepartamento": "id_departamento",
            "categoria": "categoria",
            "provincia": "provincia",
            "localidad": "localidad",
            "nombre": "nombre",
            "direccion": "domicilio",
            "CP": "codigo_postal",
            "web": "web",
            "Mail": "mail",
            "cod_area": "cod_area",
            "telefono": "numero_de_telefono"
        },
        "to_add": []
    },
    "bibliotecas": {
        "from_csv": ['cod_localidad', 'id_provincia', 'id_departamento', 'observacion',
                     'categoria', 'subcategoria', 'provincia', 'departamento', 'localidad',
                     'nombre', 'domicilio', 'piso', 'cp', 'cod_tel', 'telefono', 'mail',
                     'web', 'informacion_adicional', 'latitud', 'longitud',
                     'tipo_latitud_longitud', 'fuente', 'fecha_fundacion', 'nro_conabip',
                     'anio_actualizacion'],
        "to_keep": ['cod_localidad', 'id_provincia', 'id_departamento',
                    'categoria', 'provincia', 'localidad',
                    'nombre', 'domicilio', 'cp', 'cod_tel', 'telefono', 'mail',
                    'web'],
        "renamed": {
            "cod_localidad": "cod_localidad",
            "id_provincia": "id_provincia",
            "id_departamento": "id_departamento",
            "categoria": "categoria",
            "provincia": "provincia",
            "localidad": "localidad",
            "nombre": "nombre",
            "domicilio": "domicilio",
            "cp": "codigo_postal",
            "cod_tel": "cod_area",
            "telefono": "numero_de_telefono",
            "mail": "mail",
            "web": "web",
        },
        "to_add": []
    },
}

current = "cines"
df = read_csv(f"source-files/{current}/2025-febrero",
              f"{current}-12-02-2025.csv")

column_types = {
    "cod_localidad": "int64",
    "id_provincia": "int8",
    "id_departamento": "int32",
    "categoria": "string",
    "provincia": "string",
    "localidad": "string",
    "nombre": "string",
    "domicilio": "string",
    "codigo_postal": "string",
    "cod_area": "string",
    "numero_de_telefono": "string",
    "mail": "string",
    "web": "string",
}


def full_phone_number(row) -> str:
    if row["cod_area"]:
        return f"{row['cod_area']} {row['numero_de_telefono'].replace(" ", "-")}"
    else:
        return row["numero_de_telefono"]


def set_mail(row) -> str:
    return row["mail"] if row["mail"] else "No hay mail"


def set_cod_area(row) -> str:
    return row["cod_area"] if row["cod_area"] else "No hay cod_area"


def complete_transform(df: pd.DataFrame, df_name: str) -> pd.DataFrame:
    df = delete_columns(df, columns[df_name]["to_keep"])
    df = rename_columns(df, columns[df_name]["renamed"])
    df = define_columns_types(df, column_types)
    if df_name == "cines":
        df = add_column(df, "numero_de_telefono", str, full_phone_number)
        df = add_column(df, "mail", str, set_mail)
        df = add_column(df, "cod_area", str, set_cod_area)

    print(f"Data Frame de {df_name}")
    return df


df_museos = read_csv(f"source-files/museos/2025-febrero",
                     "museos-12-02-2025.csv")
df_final_museos = complete_transform(df_museos, "museos")

df_cines = read_csv(f"source-files/cines/2025-febrero", "cines-12-02-2025.csv")
df_final_cines = complete_transform(df_cines, "cines")

df_bibliotecas = read_csv(
    f"source-files/bibliotecas/2025-febrero", "bibliotecas-12-02-2025.csv")
df_final_bibliotecas = complete_transform(df_bibliotecas, "bibliotecas")

normalized_df = pd.concat([df_final_museos, df_final_cines,
                           df_final_bibliotecas], ignore_index=True)
# print(df_final)


def process_final(df: pd.DataFrame) -> pd.DataFrame:
    df = df.groupby(["categoria", "provincia"]
                    ).size().reset_index(name="Total")
    df = rename_columns(
        df, {"categoria": "Categoría", "provincia": "Provincia"})
    return df


combined_df = process_final(normalized_df)
# print(df_final_combinado)


def cine_df(df: pd.DataFrame) -> pd.DataFrame:
    columns_to_keep = ["provincia", "pantallas",
                       "butacas", "espacio_incaa"]
    df = delete_columns(df, columns_to_keep)
    df = df.groupby("provincia").agg(
        pantallas=("pantallas", "sum"),
        butacas=("butacas", "sum"),
        espacio_incaa=("espacio_incaa", lambda x: (x == "Si").sum())
    ).reset_index()
    df = rename_columns(df, {"provincia": "Provincia", "pantallas": "Cantidad_de_pantallas",
                        "butacas": "Cantidad_de_butacas", "espacio_incaa": "Cantidad_de_espacios_INCAA"})
    return df


df_cines_alone = cine_df(df_cines)
print(df_cines_alone)
