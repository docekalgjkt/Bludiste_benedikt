import os
from BludisteDAO_txt import BludisteDaoTxt
from BludisteDAO_csv import BludisteDaoCsv
from BludisteDAO_xml import BludisteDaoXml

class BludisteDAOFactory:
    @staticmethod
    def get_bludiste_dao(cesta_k_souboru):
        _, file_extension = os.path.splitext(cesta_k_souboru)
        file_extension = file_extension.lower().strip()  # Normalize extension for matching

        if file_extension == '.txt':
            return BludisteDaoTxt()
        elif file_extension == '.csv':
            return BludisteDaoCsv()
        elif file_extension == '.xml':
            return BludisteDaoXml()
        else:
            raise ValueError("Nepodporovaný typ souboru: očekáván '.txt', '.xml' nebo '.csv'.")
