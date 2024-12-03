import os
import csv
from bludiste_dao_interface import BludisteDaoInterface

class BludisteDaoCsv(BludisteDaoInterface):
    def nacti_bludiste(self, cesta_k_souboru):
        # zjistuje zda existuje cesta k souboru
        if not os.path.exists(cesta_k_souboru):
            raise FileNotFoundError(f"Soubor {cesta_k_souboru} nebyl nalezen.")
        # vytvoreni seznamu pro ulozeni policek
        bludiste_data = []
        # otevre soubor a precte z nej data
        with open(cesta_k_souboru, mode='r', encoding='utf-8') as soubor:
            reader = csv.reader(soubor)
            # pro kazdy radek vytvori vnoreny list s hodnotami
            for row in reader:
                bludiste_data.append([int(x) for x in row])  # Kazdou hodnotu prevede na cislo
        # vrati cely seznam s vnorenymi listy
        return bludiste_data