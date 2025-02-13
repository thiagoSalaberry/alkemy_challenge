from datetime import date
import locale


def parse_date(date: date, format: str) -> str:
    if format not in ["AAAA-m", "dd-mm-AAAA"]:
        raise ValueError(
            "❌ Formato de fecha incorrecto. Formatos disponibles: 'AAAA-m' ó 'dd-mm-AAAA'")

    match format:
        case "AAAA-m":
            locale.setlocale(locale.LC_TIME, "es_ES.UTF-8")
            return date.strftime("%Y-%B")
        case "dd-mm-AAAA":
            return date.strftime("%d-%m-%Y")
