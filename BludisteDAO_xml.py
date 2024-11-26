import xml.etree.ElementTree as Et
from BludisteDAOInterface import BludisteDAOInterface


class BludisteDaoXml(BludisteDAOInterface):
    def nacti_bludiste(self, cesta_k_souboru):
        bludiste_data = []
        strom = Et.parse(cesta_k_souboru)
        koren = strom.getroot()
        for row in koren.findall('row'):
            row_data = [int(x) for x in row.text.strip()]
            bludiste_data.append(row_data)

        return blud
iste_data