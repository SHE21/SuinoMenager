from model import Health, Nutrition


class DailyStatus():
    def __init__(self):
        self.id_daily: str = ""
        self.id_circle: str = ""
        self.date: str = ""
        self.weight: float = 0.0