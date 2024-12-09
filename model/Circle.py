from datetime import date
from model.DailyStatus import DailyStatus


class Circle():
    def __init__(
            self, id: int,
            id_uuid: str,
            circle_name: str,
            start_date: date,
            end_date: date,
            observation: str,
            daily_status: list[DailyStatus],
            is_ended: bool
            ):
        self.id: int = id
        self.id_uuid: str = id_uuid
        self.circle_name: str = circle_name
        self.start_date: date = start_date
        self.end_date: date = end_date
        self.observation: str = observation
        self.daily_status: list[DailyStatus] = daily_status
        self.is_ended: bool = is_ended