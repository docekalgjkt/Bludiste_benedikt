import tkinter
from robot import Robot

class RobotView:
    def __init__(self, robot):
        self.robot = robot

    # vykresli robota
    def draw(self, canvas):
        x, y = self.robot.position
        size = self.robot.size
        self.shape = canvas.create_oval(
            x - size, y - size, x + size, y + size, fill=self.robot.color
        )

    # prekresli robota pri kazdem kroku
    def update_position(self, canvas, new_position):
        x, y = new_position
        size = self.robot.size
        canvas.coords(
            self.shape, x - size, y - size, x + size, y + size
        )