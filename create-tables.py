from connections import conn


def read_sql(file_path: str, file_name: str) -> str:
    try:
        with open(f"{file_path}/{file_name}.sql", "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(
            f"❌ El archivo {file_name}.sql no existe en la ruta {file_path}.")


def get_query(sql_script: str, query: str) -> str:
    query = f"{sql_script.split(f"-- {query}")[1].split(";")[0]};".strip()
    return query


def run_query(query: str, return_data: bool = False, close_on_end: bool = True):
    try:
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        print(f"✅ Query executed successfully.")
        if return_data:
            return cur.fetchall()
    except Exception as e:
        print(f"❌ Error al ejecutar la query: {e}")
    finally:
        if close_on_end:
            cur.close()
            conn.close()


def create_tables(tables: list) -> None:
    for table in tables:
        sql_script = read_sql("sql", f"{table}")
        query = get_query(sql_script, "CREATE TABLE")
        run_query(query, return_data=False, close_on_end=False)
        print(f"✅ La tabla {table} se creó con éxito")
    conn.close()


def drop_tables(tables: list) -> None:
    for table in tables:
        sql_script = read_sql("sql", f"{table}")
        query = get_query(sql_script, "DROP TABLE")
        run_query(query, return_data=False, close_on_end=False)
        print(f"✅ La tabla {table} se eliminó con éxito")
    conn.close()


sql_tables = ["amount", "cinemas-data", "normalized"]

# create_tables(sql_tables)
