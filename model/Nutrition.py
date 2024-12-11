from datetime import date
from model import DailyStatus


class Nutrition(DailyStatus):
    def __init__(self,
                    id_uuid: str, 
                    id_uuid_suino: str, 
                    id_uuid_circle: str, 
                    weight: float, 
                    registration_date: date,
                    id_uuid_nutrition: str, 
                    daily_feed_intake: float, 
                    feed_composition: str, 
                    weight_gain_daily: float, 
                    water_intake: float, 
                    supplementation: str
                ):
        super().__init__(
            id_uuid=id_uuid, 
            id_uuid_suino=id_uuid_suino, 
            id_uuid_circle=id_uuid_circle, 
            weight=weight, 
            registration_date=registration_date
        )
        self.id_uuid_nutrition: str = id_uuid_nutrition
        self.daily_feed_intake: float = daily_feed_intake  # kg/day
        self.feed_composition: str = feed_composition
        self.weight_gain_daily: float = weight_gain_daily  # g/day
        self.water_intake: float = water_intake  # liters/day
        self.supplementation: str = supplementation