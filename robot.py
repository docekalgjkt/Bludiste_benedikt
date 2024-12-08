from collections import deque

class Robot:
    def __init__(self, color):
        self.color = color
        self.position = (0, 0)  # Starting position
        self.path = []  # To store the calculated path
    
    def solve_maze(self, maze):
        # Find the exit (2 represents the exit in the maze)
        start = self.position
        exit = self.find_exit(maze)
        visited = set()
        queue = deque([(start, [])])  # Queue stores (position, path)
        
        while queue:
            (x, y), path = queue.popleft()
            
            # If the exit is found, return the path
            if (x, y) == exit:
                self.path = path  # Store the path to the exit
                return path
            
            if (x, y) in visited:
                continue
            
            visited.add((x, y))
            
            # Explore neighbors (up, down, left, right)
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                # Check if within maze bounds and not a wall (1 represents a wall)
                if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] != 1:
                    queue.append(((nx, ny), path + [(nx, ny)]))
        
        return []  # No path found

    def find_exit(self, maze):
        # Search for the exit (represented by 2) in the maze
        for y, row in enumerate(maze):
            for x, cell in enumerate(row):
                if cell == 2:  # Exit found
                    return (x, y)
        return None  # Return None if no exit is found
    
    def follow_path(self):
        # Move the robot along the path
        for step in self.path:
            self.update_position(step)
            # Here, you can trigger updates in the graphical interface as well
            print(f"Robot moved to: {step}")

    def update_position(self, new_position):
        self.position = new_position
        # Update graphical view or perform other actions here