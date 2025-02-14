from utils.extraction import read_csv, get_data
from utils.transformation import complete_transform, combine, cine_df
from datetime import date
from utils.parse_dates import parse_date
import pandas as pd
from sqlalchemy import create_engine
from configparser import ConfigParser
from utils.create_tables import create_tables

# Read sensitive data
parser = ConfigParser()
parser.read("pipeline.conf")
urls_section = parser["alkemy-data"]
neon_connection_url = parser["neon"]

# Raw data
urls = {
    "museums": urls_section["MUSEUMS_URL"],
    "cinemas": urls_section["CINEMAS_URL"],
    "libraries": urls_section["LIBRARIES_URL"]
}

DB_URL = neon_connection_url["DB_URL"]


def main():
    # Day of execution
    now = date.today()
    year_month = parse_date(now, "AAAA-m")
    dd_mm_AAAA = parse_date(now, "dd-mm-AAAA")

    # Connection to database
    engine = create_engine(DB_URL)

    # Extraction
    get_data(urls, year_month, dd_mm_AAAA)

    raw_museums_data = read_csv(
        f"source-files/museums/{year_month}", f"museums-{dd_mm_AAAA}")
    raw_cinemas_data = read_csv(
        f"source-files/cinemas/{year_month}", f"cinemas-{dd_mm_AAAA}")
    raw_libraries_data = read_csv(
        f"source-files/libraries/{year_month}", f"libraries-{dd_mm_AAAA}")

    # Transformation
    museums_df = complete_transform(raw_museums_data, "museums")
    cinemas_df = complete_transform(raw_cinemas_data, "cinemas")
    libraries_df = complete_transform(raw_libraries_data, "libraries")
    print("\n")

    # Transformation to desired Data Frames
    normalized_df = pd.concat([museums_df, cinemas_df, libraries_df])
    combined_df = combine(normalized_df)
    cinemas_df = cine_df(raw_cinemas_data)

    # Creation of SQL tables
    sql_tables = ["amount", "cinemas", "normalized"]
    create_tables(sql_tables)

    # Insertion into tables
    print("\n🔼 Insertando registros en las tablas SQL...")
    normalized_df.to_sql("normalized", con=engine,
                         if_exists="replace", index=False)
    combined_df.to_sql("amount", con=engine, if_exists="replace", index=False)
    cinemas_df.to_sql("cinemas", con=engine, if_exists="replace", index=False)

    print("✨ El proceso de extracción, transformación y carga terminó.")

    print("\nTabla normalizada")
    print(normalized_df)
    print("\nTabla de categorías y provincias")
    print(combined_df)
    print("\nTabla de cines")
    print(cinemas_df)


main()
