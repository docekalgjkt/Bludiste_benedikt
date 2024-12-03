from abc import ABC, abstractmethod

# abstraktni dao trida pro dalsi konkretni dao tridy
class BludisteDaoInterface(ABC):
    @abstractmethod
    # abstraktni metoda pro nacitani dat z ruznych souboru
    def nacti_bludiste(self, cesta_k_souboru):
        pass