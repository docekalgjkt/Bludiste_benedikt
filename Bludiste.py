class Bludiste:
    # vytvoreni inicializacni metody
    def __init__(self, bludiste):
        self.bludiste = bludiste
        self.roboti_pozice = None  # promenna pro ulozeni pozice robota
        self.roboti_kontrola = None  # promenna pro kontrolu

    # metoda pro ziskani sirky bludiste
    def get_sirka(self):
        return len(self.bludiste[0])

    # metoda pro ziskani vysky bludiste
    def get_vyska(self):
        return len(self.bludiste)

    # metoda pro kontrolu dosazeni vychodu
    def je_vychod(self):
        return self.roboti_pozice == 2  # true kdyz je na policku vychod

    # kontrola volnych poli kolem robota
    def je_volno(self):
        return self.roboti_kontrola == 0 or self.roboti_kontrola == 2  # true kdyz je policko pruchozi

    # metoda pro ziskani pozice vychodu
    def get_vychod(self):
        for y, radek in enumerate(self.bludiste):
            for x, hodnota in enumerate(radek):
                if hodnota == 2:
                    return (y, x)  # index policka vychodu
        return None  # pokud vychod neni
