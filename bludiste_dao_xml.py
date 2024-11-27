import xml.etree.ElementTree as Et
from bludiste_dao_interface import BludisteDaoInterface


class BludisteDaoXml(BludisteDaoInterface):
    def nacti_bludiste(self, cesta_k_souboru):
        # vytvoreni seznamu pro ulozeni policek
        bludiste_data = []
        strom = Et.parse(cesta_k_souboru)
        koren = strom.getroot()
        # zjisti kazdou hodnotu v radku a prevede ji na cislo
        for row in koren.findall('row'):
            # z kazdeho radku vytvori seznam
            row_data = [int(x) for x in row.text.strip()]
            # kazdy seznam postupne vnoruje do bludiste_data
            bludiste_data.append(row_data)

        return bludiste_data