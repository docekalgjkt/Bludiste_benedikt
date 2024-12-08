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

        # Zavolani metody pro vyber souboru
        cesta_k_souboru = self.vyber_soubor()

        if cesta_k_souboru:
            # Pouziti DAO factory
            dao = BludisteDaoFactory.get_bludiste_dao(cesta_k_souboru)
            bludiste_data = dao.nacti_bludiste(cesta_k_souboru)

            # Vytvoreni instance tridy Bludiste
            self.bludiste = Bludiste(bludiste_data)

            # Vytvoreni instance tridy BludisteView
            self.view = BludisteView(root, self.bludiste, self.window_sirka, self.window_vyska)
            self.view.vykresli()

            # Calculate cell size based on the canvas size and maze size
            sirka_policka = self.window_sirka // self.bludiste.get_sirka()
            vyska_policka = self.window_vyska // self.bludiste.get_vyska()

            # Create robot and robot view instances
            self.robot = Robot(color="blue")  # No need to specify size
            self.robot_view = RobotView(self.robot, sirka_policka, vyska_policka)

            # Solve the maze to get the path
            self.robot.solve_maze(self.bludiste.bludiste)
            self.robot.follow_path()

            # Draw the robot at its starting position
            self.robot_view.draw(self.view.canvas)

    def vyber_soubor(self):
        # Ziskani cesty k aktualnimu adresari
        slozka = os.path.dirname(__file__)

        # Filtr pro podporovane soubory
        soubory = [f for f in os.listdir(slozka) if f.endswith(('.txt', '.xml', '.csv'))]

        if not soubory:
            print("Žádné podporované soubory nebyly nalezeny.")
            return None

        # Otevreni dialogoveho okna pro vyber souboru
        soubor = filedialog.askopenfilename(
            title="Vyberte soubor",
            initialdir=slozka,
            filetypes=[("Podporované soubory", "*.txt;*.xml;*.csv")]
        )

        return soubor


# Spusteni aplikace
def main():
    root = tk.Tk()
    root.title("Bludiste App")

    # Nastaveni rozmeru okna
    window_width = 600
    window_height = 450

    # Vytvoreni instance aplikace
    app = BludisteApp(root, window_width, window_height)

    # Spusteni hlavni smycky
    root.mainloop()


if __name__ == "__main__":
    main()
