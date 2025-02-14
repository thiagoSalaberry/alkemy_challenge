import psycopg2
from configparser import ConfigParser

parser = ConfigParser()
parser.read('pipeline.conf')
neon_data = parser["neon"]
DB_URL = neon_data["DB_URL"]

try:
    # Conectar a la base de datos
    conn = psycopg2.connect(DB_URL)

    print(f"✅ Conectado a PostgreSQL a través de Neon")

except Exception as e:
    print(f"❌ Error al conectar a PostgreSQL: {e}")
