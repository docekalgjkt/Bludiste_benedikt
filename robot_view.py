class RobotView:
    def __init__(self, robot, sirka_policka, vyska_policka):
        self.robot = robot
        self.sirka_policka = sirka_policka
        self.vyska_policka = vyska_policka
        self.shape = None  # Will hold the shape (oval) on the canvas
        
        # Calculate the size of the robot relative to the cell size
        self.robot.size = min(self.sirka_policka, self.vyska_policka) // 3  # One third of the cell size
    
    def draw(self, canvas):
        # Draw the robot at its current position
        x, y = self.robot.position
        stred_x = x * self.sirka_policka + self.sirka_policka // 2
        stred_y = y * self.vyska_policka + self.vyska_policka // 2

        size = self.robot.size
        self.shape = canvas.create_oval(
            stred_x - size, stred_y - size, stred_x + size, stred_y + size, fill=self.robot.color
        )