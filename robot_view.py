import tkinter
from robot import Robot

class RobotView:
    def __init__(self, robot, sirka_policka, vyska_policka):
        self.robot = robot
        self.sirka_policka = sirka_policka  # Width of a cell
        self.vyska_policka = vyska_policka  # Height of a cell

        # Calculate robot size as 50% of the smaller dimension of the cell
        self.robot.size = min(self.sirka_policka, self.vyska_policka) // 3  # Robot size = 50% of the cell size

    # Draw the robot at its current position, centered in the cell
    def draw(self, canvas):
        x, y = self.robot.position
        # Calculate the center of the cell for both x and y
        center_x = x * self.sirka_policka + self.sirka_policka // 2
        center_y = y * self.vyska_policka + self.vyska_policka // 2

        size = self.robot.size
        self.shape = canvas.create_oval(
            center_x - size, center_y - size, center_x + size, center_y + size, fill=self.robot.color
        )

    # Update the robot's position and redraw it at the new position
    def update_position(self, canvas, new_position):
        x, y = new_position
        # Calculate the new center of the cell for both x and y
        center_x = x * self.sirka_policka + self.sirka_policka // 2
        center_y = y * self.vyska_policka + self.vyska_policka // 2

        size = self.robot.size
        # Update the robot's position by moving the oval
        canvas.coords(
            self.shape, center_x - size, center_y - size, center_x + size, center_y + size
        )