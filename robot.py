class Robot:
    def __init__(self, color): # dodelat komunikaci s bludistem
        self.color = color
        self.position = (0, 0)  # pocatecni pozice
        self.cesta = []  # seznam pro cestu k vychodu
    
    # vyresi bludiste v pameti
    def vyres_bludiste(self, bludiste):
        pass

    # pamatuje si aktualni pozici
    def aktualni_pozice(self):
        pass