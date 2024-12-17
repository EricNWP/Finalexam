from abc import ABC, abstractmethod

class DietStrategy(ABC):
    @abstractmethod
    def feed(self, weight):
        pass