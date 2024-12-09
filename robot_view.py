class RobotView:
    def __init__(self, robot, sirka_policka, vyska_policka):
        self.robot = robot
        self.sirka_policka = sirka_policka
        self.vyska_policka = vyska_policka
        self.shape = None  # promenna pro ulozeni tvaru robota
        
        # spocita velikost robota v zavislosti na velikosti policka
        self.robot.size = min(self.sirka_policka, self.vyska_policka) // 3  # jedna tretina policka
    
    def vykresli(self, canvas):
        # vykresli robota v danem policku
        x, y = self.robot.position

        # vypocita stred policka 
        stred_x = x * self.sirka_policka + self.sirka_policka // 2
        stred_y = y * self.vyska_policka + self.vyska_policka // 2

        # vykresli oval uprostred policka
        size = self.robot.size
        self.shape = canvas.create_oval(
            stred_x - size, stred_y - size, stred_x + size, stred_y + size, fill=self.robot.color
        )