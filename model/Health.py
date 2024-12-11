from datetime import date

from model import DailyStatus


class Health(DailyStatus):
    def __init__(self):
        self.id_uui_health: str = ""
        self.medicine_name: str = ""
        self.medicine_type: str = ""
        self.adminitration_type: str =""
        self.dosage: float =""
        self.is_treatment: bool = False
        self.diagnosis: str = ""
        self.date_start: date = ""
        self.date_end: date = ""
        self.obervation: str = ""