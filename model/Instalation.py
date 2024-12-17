from datetime import date


class Instalation:
    def __init__(
        self, id, id_uuid, geo_location, address, name, area, infra, registration_date
    ):
        self.id: int = id
        self.id_uuid: str = id_uuid
        self.geo_location: list[float] = geo_location
        self.address: str = address
        self.name: str = name
        self.area: float = area
        self.infra: str = infra
        self.registration_date: date = registration_date

    def to_string(self):
        return (
            f"Model("
            f"id_uuid='{self.id_uuid}', "
            f"geo_location={self.geo_location}, "
            f"address='{self.address}', "
            f"name='{self.name}', "
            f"area={self.area}, "
            f"infra='{self.infra}'),"
            f"registration_date='{self.infra}')"
        )
