import tkinter as tk
from tkinter import filedialog
import os
from bludiste import Bludiste
from bludiste_view import BludisteView
from bludiste_dao_factory import BludisteDaoFactory


class BludisteApp:
    def __init__(self, root, window_sirka, window_vyska):
        self.root = root
        self.window_sirka = window_sirka
        self.window_vyska = window_vyska

        # Zavolani metody pro vyber souboru
        cesta_k_souboru = self.vyber_soubor()

        if cesta_k_souboru:
            # pouziti factory
            dao = BludisteDaoFactory.get_bludiste_dao(cesta_k_souboru)
            bludiste_data = dao.nacti_bludiste(cesta_k_souboru)

            # vytvoreni instance tridy bludiste
            self.bludiste = Bludiste(bludiste_data)

            # vytvoreni instance tridy bludisteview
            self.view = BludisteView(root, self.bludiste, self.window_sirka, self.window_vyska)
            self.view.vykresli()

    def vyber_soubor(self):
        # ziskani cesty k akutalnimu adresari
        slozka = os.path.dirname(__file__)

        # filtr pro podporovane soubory
        soubory = [f for f in os.listdir(slozka) if f.endswith(('.txt', '.xml', '.csv'))]

        if not soubory:
            print("Žádné podporované soubory nebyly nalezeny.")
            return None

        # otevreni dialogoveho okna pro vyber souboru
        soubor = filedialog.askopenfilename(
            title="Vyberte soubor",
            initialdir=slozka,
            filetypes=[("Podporované soubory", "*.txt;*.xml;*.csv")]
        )

        return soubor


# spusteni aplikace
def main():
    root = tk.Tk()
    root.title("Bludiste App")

    # nastaveni rozmeru okna
    window_width = 600
    window_height = 450

    # vytvoreni instance aplikace
    app = BludisteApp(root, window_width, window_height)

    # spusteni hlavni smycky
    root.mainloop()


if __name__ == "__main__":
    main()