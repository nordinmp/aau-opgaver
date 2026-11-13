import random
from tracemalloc import start

from matplotlib.cm import terrain
import pygame



class TerrainType:
    def __init__(self, name, grid, color = (0, 255, 0)):
        self.name = name
        self.color = color
        self.grid = grid
    
    def generate_grid(self):
        row = []
        for x in range(self.grid[1]):
            column = []

            for y in range(self.grid[0]):
            
                column.append("0")
            row.append(column)
        return row

    def draw_path(self, grid, path):
        new_grid = []
        for row in grid:
            new_grid.append(row.copy())

        for coord in path:
            x, y = coord
            new_grid[y][x] = "3"

        return new_grid


    def draw_terrain(self, coord, radius, grid, terrain_type):
        x, y = coord

        if terrain_type == "water":
            terrain_value = "2"
        if terrain_type == "mountain":
            terrain_value = "1"


        # copy grid, for new grid that can be manipulated
        new_grid = []
        for row in grid:
            new_grid.append(row.copy())

        # if x,y are not between 0 and the length of grid, return
        if not (0 <= y < len(new_grid) and 0 <= x < len(new_grid[0])):
            return new_grid


        # find the areas within the radius and mark them as water, by generating points around the center
        for row in range(max(0, y - radius), min(len(new_grid), y + radius + 1)):
            for column in range(max(0, x - radius), min(len(new_grid[0]), x + radius + 1)):

                # function for circle, to check if point is in radius
                if (x - column) ** 2 + (y - row) ** 2 <= radius ** 2:
                    # if in circle draw as water
                    new_grid[row][column] = terrain_value

        return new_grid

    def draw_grid_on_screen(self, screen, grid):
        rows = len(grid)
        columns = len(grid[0])

        for x in range(rows):
            for y in range(columns):
                if grid[x][y] == "0":
                    pygame.draw.rect(screen, (0,255,0), (y * 10, x * 10, 10, 10))
                elif grid[x][y] == "1":
                    pygame.draw.rect(screen, (139, 69, 19), (y * 10, x * 10, 10, 10))
                elif grid[x][y] == "2":
                    pygame.draw.rect(screen, (0,0,255), (y * 10, x * 10, 10, 10))
                elif grid[x][y] == "3":
                    pygame.draw.rect(screen, (255,255,0), (y * 10, x * 10, 10, 10))

class Point:
    def __init__(self, coord, color):
        self.x, self.y = coord
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x * 10, self.y * 10, 10, 10))

    def update_position(self, new_coord):
        self.x, self.y = new_coord

class Pathfinding:
    def __init__(self, grid):
        self.grid = grid

    def _get_neighbors(self, grid, current):
        # get the neighboring grid posistions
        x, y = current
        neighbors = []

        # go through each direction
        for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            next_x = x + dx
            next_y = y + dy

            # Check that the neighbor is inside the grid.
            if 0 <= next_y < len(grid) and 0 <= next_x < len(grid[0]):
                neighbors.append((next_x, next_y))

        return neighbors

    def _terrain_cost(self, grid, position):
        # return the cost for each terrain type
        x, y = position
        costs = {
            "0": 1,  # Grass
            "2": 2,  # Water
            "1": 3,  # Mountain
            "3": 1,  # Path
        }
        return costs[grid[y][x]]

    def _heuristic(self, a, b):
        # Manhattan distance on a square grid
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def pathfinding(self, grid, start, end):
        # positiion and the cost to reach it from the start
        frontier = [(start, 0)]

        # remeber the path
        came_from = {}
        came_from[start] = None

        # remeber the cost to reach each pos
        cost_so_far = {}
        cost_so_far[start] = 0

        while frontier:
            # sort so that the cheapest poisition comes first, then remove
            frontier.sort(key=lambda item: item[1])
            current, current_cost = frontier.pop(0)

            # if current reached the end, break the loop
            if current == end:
                break

            for next in self._get_neighbors(grid, current):
                # calculate the cost of moving through different terrain types
                new_cost = cost_so_far[current] + self._terrain_cost(grid, next)

                # if the new cost is lower than the previous cost, update it

                # if the new calculated cost is lower than the current cost, update the cost
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    # calculate the priotiy for the next posisiton using manhatten distance heuristic
                    priority = new_cost + self._heuristic(next, end)
                    frontier.append((next, priority))
                    # save how this position was reached for path reconstruction
                    came_from[next] = current

        path = []

        # go from end to start, following the came_from to get shortest path
        current = end
        while current is not None:
            path.append(current)
            current = came_from[current]

        # return reversed path
        return path[::-1]


def draw_everything(screen, terrain, grid, startpoint, endpoint, pathfinder):

    path = pathfinder.pathfinding(
        grid,
        (startpoint.x, startpoint.y),
        (endpoint.x, endpoint.y),
    )


    terrain.draw_grid_on_screen(screen, grid) # draw grid
    terrain.draw_path(grid, path) # draw path
    terrain.draw_grid_on_screen(screen, terrain.draw_path(grid, path)) # add path to grid
    startpoint.draw(screen) # draw startpoint
    endpoint.draw(screen) # draw endpoint


def place_terrain(terrain, grid):
    # draw random water areas on the grid
    for i in range(random.randint(15, 35)):
        x = random.randint(0, terrain.grid[0] - 1)
        y = random.randint(0, terrain.grid[1] - 1)
        radius = random.randint(1, 10)

        grid = terrain.draw_terrain((x, y), radius, grid, "water")

    # draw random mountain areas on the grid
    for i in range(random.randint(4,8)):
        x = random.randint(0, terrain.grid[0] - 1)
        y = random.randint(0, terrain.grid[1] - 1)
        radius = random.randint(10, 15)

        grid = terrain.draw_terrain((x, y), radius, grid, "mountain")

    return grid


def main():
    pygame.init()

    screen_size = (1920, 1080)

    screen = pygame.display.set_mode(screen_size)

    terrain = TerrainType("grass", (screen_size[0]//10, screen_size[1]//10), (0, 255, 0))

    pathfinder = Pathfinding(terrain.grid)

    grid = terrain.generate_grid()

    grid = place_terrain(terrain, grid)

    startpoint = Point((10, 45), (0, 255, 255))
    endpoint = Point((45, 20), (255, 0, 0))


    draw_everything(screen, terrain, grid, startpoint, endpoint, pathfinder)

    run_flag = True

    # dragging varaible to see what point is being dragged
    dragging = None
    
    while run_flag is True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_flag = False

            # if check if the left mouse button is being pressed down
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                # convert mouse coord to grid coord
                grid_x, grid_y = event.pos[0] // 10, event.pos[1] // 10

                # if grid coord are the same as the start or end point, set dragging to that point
                if (startpoint.x, startpoint.y) == (grid_x, grid_y):
                    dragging = startpoint
                elif (endpoint.x, endpoint.y) == (grid_x, grid_y):
                    dragging = endpoint

            # if the left mouse button is released, set dragging to None
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                dragging = None

            # if the mouse is moving and there is a point selected
            elif event.type == pygame.MOUSEMOTION and dragging is not None:

                # uodate grid coords to mouse coords
                grid_x, grid_y = event.pos[0] // 10, event.pos[1] // 10

                # update pos of the dragged point
                dragging.update_position((grid_x, grid_y))

                draw_everything(screen, terrain, grid, startpoint, endpoint, pathfinder)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    # regenerate grid
                    grid = terrain.generate_grid()

                    grid = place_terrain(terrain, grid)

                    # recalc path
                    draw_everything(screen, terrain, grid, startpoint, endpoint, pathfinder)

        pygame.display.flip() # Refresh the screen so drawing appears

if __name__ == "__main__":
    main()