from datetime import date, datetime
from ctypes import windll, Structure, c_long, byref

class RECT(Structure):
    _fields_ = [("left", c_long),
                ("top", c_long),
                ("right", c_long),
                ("bottom", c_long)]

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
    
def get_taskbar_dimensions() -> int:
        # Obtém a área de trabalho (sem a barra de tarefas)
        work_area = RECT()
        windll.user32.SystemParametersInfoW(48, 0, byref(work_area), 0)  # SPI_GETWORKAREA = 48

        screen_height = windll.user32.GetSystemMetrics(1)  # Altura da tela

        # Calcula a largura e altura da barra de tarefas
        return screen_height - (work_area.bottom - work_area.top)

if __name__ == "__main__":
    calculate_days("2024-12-9", "2024-12-15")


