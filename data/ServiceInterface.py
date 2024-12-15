from abc import ABC, abstractmethod

from model.DailyStatus import DailyStatus


class ServiceInterface(ABC):
    @abstractmethod
    def create(self, daily_status: DailyStatus):
        pass
