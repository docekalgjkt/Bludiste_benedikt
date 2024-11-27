import os
import csv
from bludiste_dao_interface import BludisteDaoInterface

class BludisteDaoCsv(BludisteDaoInterface):
    def nacti_bludiste(self, cesta_k_souboru):
        # zjistuje zda existuje cesta k souboru
        if not os.path.exists(cesta_k_souboru):
            raise FileNotFoundError(f"Soubor {cesta_k_souboru} nebyl nalezen.")
        # ulozeni interpretace dat
        bludiste_data = []
        with open(cesta_k_souboru, mode='r', encoding='utf-8') as soubor:
            reader = csv.reader(soubor)
            for row in reader:
                bludiste_data.append([int(x) for x in row])  # Convert each value to int
        return bludiste_data