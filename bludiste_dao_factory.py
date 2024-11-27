import os
from bludiste_dao_txt import BludisteDaoTxt
from bludiste_dao_csv import BludisteDaoCsv
from bludiste_dao_xml import BludisteDaoXml

class BludisteDaoFactory:
    @staticmethod
    def get_bludiste_dao(cesta_k_souboru):

        _, file_extension = os.path.splitext(cesta_k_souboru)   # zjisteni typu souboru podle pripony
        file_extension = file_extension.lower().strip()  # prevede na potrebny format (".xxx")
        # vybere konkretni DAO podle typu souboru
        if file_extension == '.txt':
            return BludisteDaoTxt()
        elif file_extension == '.csv':
            return BludisteDaoCsv()
        elif file_extension == '.xml':
            return BludisteDaoXml()
        # zobrazi pokud neni typ souboru podporovan 
        else:
            raise ValueError("Nepodporovaný typ souboru: očekáván '.txt', '.xml' nebo '.csv'.")
