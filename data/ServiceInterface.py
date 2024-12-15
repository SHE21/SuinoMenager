from abc import ABC, abstractmethod

from model.Circle import Circle
from model.DailyStatus import DailyStatus


class ServiceInterface(ABC):
    @abstractmethod
    def create(self, daily_status: DailyStatus):
        pass

    @abstractmethod
    def get_daily_status_by_circle(
        self, circle: Circle
    ) -> list[DailyStatus]:
        pass
