from abc import abstractmethod
from datetime import date
from model.DailyStatus import DailyStatus


class Circle:
    def __init__(
        self,
        id: int,
        id_uuid: str,
        id_uuid_baia: str,
        circle_name: str,
        start_date: date,
        end_date: date,
        observation: str,
        daily_status: list[DailyStatus],
        is_ended: bool,
        registration_date=date,
    ):
        self.id: int = id
        self.id_uuid: str = id_uuid
        self.id_uuid_baia: str = id_uuid_baia
        self.circle_name: str = circle_name
        self.start_date: date = start_date
        self.end_date: date = end_date
        self.observation: str = observation
        self.daily_status: list[DailyStatus] = daily_status
        self.is_ended: bool = (is_ended,)
        self.registration_date: date = registration_date


def get_list_circle_name(list: list[Circle]):
    result = []

    for circle in list:
        result.append(circle.circle_name)

    return result
