def get_query(sql_script: str, query: str) -> str:
    query = f"{sql_script.split(f"-- {query}")[1].split(";")[0]};".strip()
    return query
