from abc import ABC, abstractmethod

class BludisteDAO(ABC):
    @abstractmethod
    def precti_data(self):
        pass

    @abstractmethod
    def uloz_data(self, bludiste):
        pass
