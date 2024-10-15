class Bludiste:

    def __init__(self, bludiste):
        self.bludiste = bludiste

    def get_sirka(self) -> int:
        sirka = len(self.bludiste[0])  # Width of the maze
        return sirka

    def get_vyska(self) -> int:
        vyska = len(self.bludiste)  # Height of the maze
        return vyska

    def get_vychod(self):
        # Iterate over the rows and columns to find the exit (2)
        for y in range(len(self.bludiste)):  # Loop through rows
            for x in range(len(self.bludiste[y])):  # Loop through columns
                if self.bludiste[y][x] == 2:  # Exit found
                    return [x, y]  # Return the coordinates as (x, y)

                else:
                    return None  # If no exit is found

    def je_vychod(self) -> bool:
        pass

bludiste_list = [[0, 1, 1], [0, 1, 0], [0, 0, 2]]

bludiste = Bludiste(bludiste_list)

print(f"Sirka bludiste: {bludiste.get_sirka()}")
print(f"Vyska bludiste: {bludiste.get_vyska()}")