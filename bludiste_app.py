import tkinter as tk
from tkinter import filedialog
import os
from bludiste import Bludiste
from bludiste_view import BludisteView
from bludiste_dao_factory import BludisteDaoFactory
from robot import Robot
from robot_view import RobotView


class BludisteApp:
    def __init__(self, root, window_width, window_height):
        self.root = root
        self.window_sirka = window_width
        self.window_vyska = window_height

        # zavola metodu pro vyber souboru
        cesta_k_souboru = self.vyber_soubor()

        # pokud najde soubor pokracuje dal
        if cesta_k_souboru:
            # pouzije DAO factory pro spravnou interpretaci dat
            dao = BludisteDaoFactory.get_bludiste_dao(cesta_k_souboru)
            bludiste_data = dao.nacti_bludiste(cesta_k_souboru)

            # vytvori instanci tridy Bludiste
            self.bludiste = Bludiste(bludiste_data)

            # vytvori instanci tridy BludisteView
            self.view = BludisteView(root, self.bludiste, self.window_sirka, self.window_vyska)
            self.view.vykresli()

            # vypocita sirku a vysku policka
            sirka_policka = self.window_sirka // self.bludiste.get_sirka()
            vyska_policka = self.window_vyska // self.bludiste.get_vyska()

            # vytvori instance trid Robot a RobotView
            self.robot = Robot(color="blue")
            self.robot_view = RobotView(self.robot, sirka_policka, vyska_policka)

            # vykresli robota na startovni pozici (0, 0)
            self.robot_view.vykresli(self.view.canvas)

            # vyresi si v pameti bludiste - musim dodelat algoritmus
            self.robot.vyres_bludiste(self.bludiste)

            # to-do: DODELAT PRUCHOD BLUDISTE KROK ZA KROKEM

    def vyber_soubor(self):
        # ziska cestu k aktualni slozce
        slozka = os.path.dirname(__file__)

        # Vyfiltruje podporovane soubory
        soubory = [f for f in os.listdir(slozka) if f.endswith(('.txt', '.xml', '.csv'))]

        if not soubory:
            print("Žádné podporované soubory nebyly nalezeny.")
            return None

        # otevre slozku pro vyber podporovaneho souboru
        soubor = filedialog.askopenfilename(
            title="Vyberte soubor",
            initialdir=slozka,
            filetypes=[("Podporované soubory", "*.txt;*.xml;*.csv")]
        )

        return soubor


# Spusteni aplikace
def main():
    root = tk.Tk()
    root.title("Bludiště App")

    # Rozmery okna
    window_width = 600
    window_height = 450

    # vytvoreni instance aplikace
    app = BludisteApp(root, window_width, window_height)

    # zahajeni hlavni smycky
    root.mainloop()


if __name__ == "__main__":
    main()
