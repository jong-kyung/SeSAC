from abc import ABC, abstractmethod

class Info(ABC):
    @abstractmethod
    def get_info(self):
        pass