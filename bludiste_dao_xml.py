import xml.etree.ElementTree as Et
from bludiste_dao_interface import BludisteDaoInterface


class BludisteDaoXml(BludisteDaoInterface):
    def nacti_bludiste(self, cesta_k_souboru):
        bludiste_data = []
        strom = Et.parse(cesta_k_souboru)
        koren = strom.getroot()
        for row in koren.findall('row'):
            row_data = [int(x) for x in row.text.strip()]
            bludiste_data.append(row_data)

        return bludiste_data