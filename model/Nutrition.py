from model import DailyStatus


class Nutrition(DailyStatus):
    def __init__(self):
        self.id_uuid_nutrition: str = ""
        self.daily_feed_intake: float = 0.0  # kg/day
        self.feed_composition: str = "feed_composition"
        self.weight_gain_daily: float = 0.0  # g/day
        self.water_intake: float = 0.0  # liters/day
        self.supplementation: str = "supplementation"