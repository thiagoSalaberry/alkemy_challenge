import pandas as pd
from utils.transformation import delete_columns, define_columns_types, add_column, rename_columns, full_phone_number, set_cod_area, set_mail, columns, column_types
from utils.extraction import read_csv

raw_museums_df = read_csv(
    "source-files/museums/2025-febrero", "museums-14-02-2025")
raw_cinemas_df = read_csv(
    "source-files/cinemas/2025-febrero", "cinemas-14-02-2025")
raw_libraries_df = read_csv(
    "source-files/libraries/2025-febrero", "libraries-14-02-2025")

museums_df = delete_columns(raw_museums_df, columns["museums"]["to_keep"])
museums_df = rename_columns(museums_df, columns["museums"]["renamed"])
museums_df = museums_df.where(pd.notna(museums_df), None)
museums_df = define_columns_types(museums_df, column_types)
print(museums_df)

cinemas_df = delete_columns(raw_cinemas_df, columns["cinemas"]["to_keep"])
cinemas_df = rename_columns(cinemas_df, columns["cinemas"]["renamed"])
cinemas_df = cinemas_df.where(pd.notna(cinemas_df), None)
cinemas_df = define_columns_types(cinemas_df, column_types)
cinemas_df = add_column(cinemas_df, "cod_area", str, set_cod_area)
cinemas_df = add_column(
    cinemas_df, "numero_de_telefono", str, full_phone_number)
cinemas_df = add_column(cinemas_df, "mail", str, set_mail)
print(cinemas_df)

libraries_df = delete_columns(
    raw_libraries_df, columns["libraries"]["to_keep"])
libraries_df = rename_columns(libraries_df, columns["libraries"]["renamed"])
libraries_df = libraries_df.where(pd.notna(libraries_df), None)
libraries_df = define_columns_types(libraries_df, column_types)
print(libraries_df)
