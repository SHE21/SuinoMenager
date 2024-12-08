from abc import ABC, abstractmethod

from model.Suino import Suino


class OnClickListener(ABC):
    @abstractmethod
    def onClick(suino: str):
        pass
