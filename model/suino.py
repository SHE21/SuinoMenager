class Suino:
    def __init__(
        self,
        id: int,
        id_uuid: str,
        id_uuid_circle: str,
        id_tag: str,
        race: str,
        date_birth: str,
        gender: str,
        origin: str,
        is_active: bool,
        registration_date: str,
    ):
        self.id: int = id
        self.id_uuid: str = id_uuid
        self.id_uuid_circle = id_uuid_circle
        self.id_tag: str = id_tag
        self.race: str = race
        self.date_birth: str = date_birth
        self.gender: str = gender
        self.origini: str = origin
        is_active: bool = is_active
        self.registration_date: str = registration_date
