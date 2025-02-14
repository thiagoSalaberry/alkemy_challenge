import requests
import os
import pandas as pd


def download_csv(csv_url: str) -> bytes:
    try:
        response = requests.get(csv_url)
        if response.status_code == 200:
            csv_data: bytes = response.content
            print("⬇ El archivo .csv se descargó con éxito.")
            return csv_data
        else:
            print(
                f"❌ Error al descargar el archivo .csv: {response.status_code}")
    except Exception as e:
        print(f"❌ Excepción al descargar el archivo .csv: {e}")


def save_file(file_path: str, file_name: str, csv_data: bytes) -> None:
    try:
        os.makedirs(file_path, exist_ok=True)

        file_path = os.path.join(file_path, file_name)

        with open(file_path, "wb") as file:
            file.write(csv_data)

    except Exception as e:
        print(f"❌ Error al guardar el archivo: {e}")


def read_csv(file_path: str, file_name: str) -> pd.DataFrame:
    """Lee un archivo CSV y devuelve un DataFrame con los datos del archivo."""
    try:
        return pd.read_csv(f"{file_path}/{file_name}.csv")
    except FileNotFoundError as e:
        print(
            f"Error al leer el archivo {file_name}: {str(e)}")


def get_data(urls: dict, year_month: str, dd_mm_AAAA: str) -> None:
    for category, url in urls.items():
        # Descargamos los archivos
        csv_data = download_csv(url)

        # Definimos la ruta de guardado
        file_path = f"source-files/{category}/{year_month}"
        file_name = f"{category}-{dd_mm_AAAA}.csv"

        # Guardamos los archivos en local
        save_file(file_path, file_name, csv_data)

    print(f"\n💾 Los archivos se guardaron correctamente en 📂 /source-files.\n")
