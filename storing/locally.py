import os


def save_file(file_path: str, file_name: str, csv_data: bytes) -> None:
    try:
        os.makedirs(file_path, exist_ok=True)

        file_path = os.path.join(file_path, file_name)

        with open(file_path, "wb") as file:
            file.write(csv_data)
            print(f"✅ Archivo guardado en: {file_path}.")

    except Exception as e:
        print(f"❌ Error al guardar el archivo: {e}")
