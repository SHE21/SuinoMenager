from model import DailyStatus


class Nutrition(DailyStatus):
    def __init__(self, 
                 id_uuid_nutrition: str, 
                 daily_feed_intake: float, 
                 feed_composition: str, 
                 weight_gain_daily: float, 
                 water_intake: float, 
                 supplementation: str
                ):
        self.id_uuid_nutrition: str = id_uuid_nutrition
        self.daily_feed_intake: float = daily_feed_intake  # kg/day
        self.feed_composition: str = feed_composition
        self.weight_gain_daily: float = weight_gain_daily  # g/day
        self.water_intake: float = water_intake  # liters/day
        self.supplementation: str = supplementation