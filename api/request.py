from configparser import ConfigParser
import requests
import pandas as pd
from io import StringIO

# parser = ConfigParser()
# parser.read("../pipeline.conf")
# project_data = parser["alkemy"]

# MUSEOS_URL: str = project_data["MUSEOS_URL"]
# CINES_URL: str = project_data["CINES_URL"]
# BIBLIOS_URL: str = project_data["BIBLIOS_URL"]


def download_csv(csv_url: str) -> bytes:
    try:
        response = requests.get(csv_url)
        if response.status_code == 200:
            csv_data: bytes = response.content
            return csv_data
        else:
            print(
                f"❌ Error al descargar el archivo .csv: {response.status_code}")
    except Exception as e:
        print(f"❌ Excepción al descargar el archivo .csv: {e}")
