from model.DailyStatus import DailyStatus


class Circle():
    def __init__(self):
        self.name = ""
        self.start_date = ""
        self.end_date = ""
        self.observation = ""
        self.daily_status: list[DailyStatus] = []