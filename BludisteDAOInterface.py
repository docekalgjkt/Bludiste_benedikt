from abc import ABC, abstractmethod

# abstraktni trida pro dalsi konkretni dao tridy
class BludisteDAOInterface(ABC):
    @abstractmethod
    def nacti_bludiste(self, cesta_k_souboru):
        pass