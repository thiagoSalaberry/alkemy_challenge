import psycopg2

DB_URL = "postgresql://neondb_owner:npg_NcMoxtAnV02E@ep-cold-brook-a4h965ik-pooler.us-east-1.aws.neon.tech/neondb?sslmode=require"

try:
    # Conectar a la base de datos
    conn = psycopg2.connect(DB_URL)

    print(f"✅ Conectado a PostgreSQL")

except Exception as e:
    print(f"❌ Error al conectar a PostgreSQL: {e}")
