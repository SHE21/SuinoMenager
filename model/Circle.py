from model.DailyStatus import DailyStatus


class Circle():
    def __init__(self):
        self.id_tag: str = ""
        self.id: int = 0
        self.name: str = ""
        self.start_date: str = ""
        self.end_date: str = ""
        self.observation: str = ""
        self.daily_status: list[DailyStatus] = []