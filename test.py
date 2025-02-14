from datetime import date
from storing.locally import save_file
from utils.extraction import download_csv
from utils.parse_dates import parse_date
from configparser import ConfigParser

parser = ConfigParser()
parser.read("pipeline.conf")
project_data = parser["alkemy-data"]

MUSEOS_URL: str = project_data["MUSEOS_URL"]
CINES_URL: str = project_data["CINES_URL"]
BIBLIOTECAS_URL: str = project_data["BIBLIOTECAS_URL"]

urls = {
    "cines": CINES_URL,
    "museos": MUSEOS_URL,
    "bibliotecas": BIBLIOTECAS_URL
}


def main() -> None:
    # Descargamos los archivos fuente
    for name, url in urls.items():
        data = download_csv(url)

        # Obtenemos la fecha de hoy
        now = date.today()
        try:
            year_month = parse_date(now, "AAAA-m")
            day_month_year = parse_date(now, "dd-mm-AAAA")
        except ValueError as e:
            print(e)
            return

        # Definimos el nombre de la carpeta y del archivo
        category = name
        file_path = f"{category}/{year_month}"
        file_name = f"{category}-{day_month_year}.csv"

        # Guardamos en la ruta source-files
        save_file(f"source-files/{file_path}", file_name, data)


main()
