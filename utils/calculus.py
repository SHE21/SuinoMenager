from datetime import date, datetime


def calculate_days(start_date: date, end_date: date) -> int:
    formatt = "%Y-%m-%d"
    try:
        # Converter as datas de string para objetos datetime
        start = datetime.strptime(start_date, formatt)
        end = datetime.strptime(end_date, formatt)

        # Calcular a diferença entre as datas
        return abs((start - end).days)
    except ValueError:
        print("Formato de data inválido! Use o formato dd/mm/aaaa.")
        return 0

if __name__ == "__main__":
    calculate_days("2024-12-9", "2024-12-15")
