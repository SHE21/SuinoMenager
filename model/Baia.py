from datetime import date


class Baia:
    def __init__(
        self,
        id: int,
        id_uuid: str,
        id_uuid_instalation: str,
        label: str,
        dimen_with: float,
        dimen_height: float,
        type_occupation: str,
        status: bool,
        registration_date: date,
    ):
        self.id = id
        self.id_uuid = id_uuid
        self.id_uuid_instalation = id_uuid_instalation
        self.label = label
        self.dimen_with = dimen_with
        self.dimen_height = dimen_height
        self.type_occupation = type_occupation
        self.status = status
        self.registration_date = registration_date

    def to_string(self):
        return (
            f"Baia("
            f"id={self.id}, "
            f"id_uuid='{self.id_uuid}', "
            f"id_uuid_instalation='{self.id_uuid_instalation}', "
            f"label='{self.label}', "
            f"dimen_with={self.dimen_with:.2f}, "
            f"dimen_height={self.dimen_height:.2f}, "
            f"type_occupation='{self.type_occupation}', "
            f"status={'Ativo' if self.status else 'Inativo'}, "
            f"registration_date={self.registration_date.strftime('%Y-%m-%d')}"
            f")"
        )
