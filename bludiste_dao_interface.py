from abc import ABC, abstractmethod

# abstraktni trida pro dalsi konkretni dao tridy
class BludisteDaoInterface(ABC):
    @abstractmethod
    def nacti_bludiste(self, cesta_k_souboru):
        pass