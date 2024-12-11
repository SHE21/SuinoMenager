from datetime import date


class DailyStatus:
    def __init__(
        self,
        id: int,
        id_uuid: str,
        id_uuid_suino: str,
        id_uuid_circle: str,
        weight: float,
        registration_date: date,
    ):
        self.id: int = id
        self.id_uuid: str = id_uuid
        self.id_uuid_suino: str = id_uuid_suino
        self.id_uuid_circle: str = id_uuid_circle
        self.weight: float = weight
        self.registration_date: date = registration_date
