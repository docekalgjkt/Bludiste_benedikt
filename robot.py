from collections import deque

class Robot:
    def __init__(self, color):
        self.color = color
        self.position = (0, 0)  # Starting position
        self.path = []  # List to store the path to the exit
    
    def vyres_bludiste(self, bludiste):
    # Simple BFS to find the shortest path (you can replace this with other algorithms)
        start = self.position
        end = bludiste.get_vychod()  # Get the exit using the Bludiste method
        queue = deque([(start, [])])  # Queue to store positions and the path taken to reach them
        visited = set()
        visited.add(start)

        while queue:
            current_position, current_path = queue.popleft()
            x, y = current_position

            # Check if we've reached the end
            if current_position == end:
                self.path = current_path + [current_position]
                return

            # Explore neighbors (up, down, left, right)
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < len(bludiste.bludiste) and 0 <= new_y < len(bludiste.bludiste[0]) and (new_x, new_y) not in visited and bludiste.bludiste[new_x][new_y] != 1:  # 1 is a wall
                    visited.add((new_x, new_y))
                    queue.append(((new_x, new_y), current_path + [current_position]))


    def projdi_bludiste(self):
        # Move the robot step by step along the path
        if self.path:
            self.position = self.path.pop(0)  # Pop the first step from the path
            return True
        return False