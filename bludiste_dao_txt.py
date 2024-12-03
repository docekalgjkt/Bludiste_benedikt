import os
from bludiste_dao_interface import BludisteDaoInterface

# konkretni trida pro nacteni z .txt souboru
class BludisteDaoTxt(BludisteDaoInterface):
    # zjistuje zda existuje cesta k souboru
    def nacti_bludiste(self, cesta_k_souboru):
        if not os.path.exists(cesta_k_souboru):
            raise FileNotFoundError(f"Soubor {cesta_k_souboru} nebyl nalezen.")
        # vytvoreni seznamu pro ulozeni policek
        bludiste_data = []
        # otevre soubor a precte z nej hodnoty
        with open(cesta_k_souboru, 'r') as soubor:
            for radek in soubor:
                # kazdou hodnotu prevede na cislo
                radek_data = [int(x) for x in radek.strip()]
                # pridava do seznamu jednotlive vnorene listy
                bludiste_data.append(radek_data)
        
        return bludiste_data
