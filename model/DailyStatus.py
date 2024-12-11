from datetime import date


class DailyStatus():
    def __init__(self):
        self.id: int = 0
        self.id_uuid: str = ""
        self.id_uuid_suino: str = ""
        self.id_uuid_circle: str = ""
        self.weight: float = 0.0
        self.registration_date: date