class Robot:

    def __init__(self, color, size):
        self.color = color # type: ignore
        self.size = size # type: ignore
        self.position = (0, 0)  # defaultni pozice robota
        self.path = []
    
    # aktualni pozice robota
    def set_position(self, x, y):
        self.position = (x, y)

    # propocita cestu a ulozi jednotlive kroky do seznamu
    def calculate_path(self, path):
        self.path = path

    # vykonava jednotlive kroky v ceste
    def move_robot(self):
        if self.path:
            self.position = self.path.pop(0)  # provede posledni krok v seznamu a odstrani ho