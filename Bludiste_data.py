class Bludiste:

    def __init__(self, bludiste):
        self.bludiste = bludiste

    def get_sirka(self) -> int:
        sirka = len(self.bludiste[0])  # Sirka bludiste
        return sirka

    def get_vyska(self) -> int:
        vyska = len(self.bludiste)  # Vyska bludiste
        return vyska

    def get_vychod(self):
        # Projde radky a sloupce bludiste a najde vychod (2)
        for y in range(len(self.bludiste)):  # Projde radky
            for x in range(len(self.bludiste[y])):  # Projde sloupce
                if self.bludiste[y][x] == 2:  # Vychod nalezen
                    return [x, y]  # Vrati souradnice vychodu

                else:
                    return None  # Pokud neni nalezen vychod

    def je_vychod(self) -> bool:
        pass

bludiste_list = [[0, 1, 1], [0, 1, 0], [0, 0, 2]]

bludiste = Bludiste(bludiste_list)

print(f"Sirka bludiste: {bludiste.get_sirka()}")
print(f"Vyska bludiste: {bludiste.get_vyska()}")