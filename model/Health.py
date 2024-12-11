from datetime import date

from model import DailyStatus


class Health(DailyStatus):
    def __init__(self,
                 id_uui_health: str,
                medicine_name: str,
                medicine_type: str,
                adminitration_type: str,
                dosage: float,
                is_treatment: bool,
                diagnosis: str,
                date_start: date,
                date_end: date,
                obervation: str
            ):
        self.id_uui_health: str = id_uui_health
        self.medicine_name: str = medicine_name
        self.medicine_type: str = medicine_type
        self.adminitration_type: str = adminitration_type
        self.dosage: float = dosage
        self.is_treatment: bool = is_treatment
        self.diagnosis: str = diagnosis
        self.date_start: date = date_start
        self.date_end: date = date_end
        self.obervation: str = obervation