import tkinter as tk

class BludisteView:
    def __init__(self, root, bludiste, canvas_sirka, canvas_vyska):
        self.root = root
        self.bludiste = bludiste
        self.canvas_sirka = canvas_sirka
        self.canvas_vyska = canvas_vyska

        # vytvoreni canvas
        self.canvas = tk.Canvas(self.root, width=self.canvas_sirka, height=self.canvas_vyska)
        self.canvas.pack()

    def vykresli(self):
        data = self.bludiste.bludiste
        sirka = self.bludiste.get_sirka()
        vyska = self.bludiste.get_vyska()

        sirka_policka = self.canvas_sirka // sirka
        vyska_policka = self.canvas_vyska // vyska

        for y, radek in enumerate(data):
            for x, hodnota in enumerate(radek):
                color = 'white' if hodnota == 0 else 'black' # projde seznam a urci barvu podle typu policek
                if hodnota == 2:
                    color = 'red'  # vychod je vybarven cervene

                x1, y1 = x * sirka_policka, y * vyska_policka
                x2, y2 = x1 + sirka_policka, y1 + vyska_policka
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)