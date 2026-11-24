import random
from turtle import width

from matplotlib.pylab import ndarray
import pygame

class City:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def generateCity(self):
        """Create a map of size width x height."""

        self.cityMap = []

        for y in range(self.height):
            row = []
            for x in range(self.width):
                row.append(".")
            self.cityMap.append(row)

        # Place a starting intersection in the upper third of the map
        currX = self.width // 3 
        currY = self.height // 3
        self.cityMap[currY][currX] = '+'

        # Generate roads in all directions
        self.newRoad((currX,currY),'u')
        self.newRoad((currX,currY),'d')
        self.newRoad((currX,currY),'l')
        self.newRoad((currX,currY),'r')


        return self.cityMap

    def newRoad(self,currentPosition, direction):

        print("New road at: ", currentPosition, " in direction: ", direction)

        """Creates a new road in direction. Direction can be 'u','d','l','r'."""
        if direction == 'u':
            vector = (0,-1)
            directionChar = '|'
        elif direction == 'd':
            vector = (0,1)
            directionChar = '|'
        elif direction == 'l':
            vector = (-1,0)
            directionChar = '-'
        else:
            vector = (1,0)
            directionChar = '-'

        # Originally, this was intended as a random road length. However, this created
        # unpredictable results. Therefore, we changed to a constant.
        randRoad = 5


        for index in range(1,randRoad):
            currX = index*vector[0] + currentPosition[0]
            currY = index*vector[1] + currentPosition[1]

            # If we are outside the width of the map, simply return
            if currX >= self.width or currX <0 or currY >= self.height or currY <0:
                return

            if self.cityMap[currY][currX] == '.':
                self.cityMap[currY][currX] = directionChar
            
        # Move to the next spot
        currX = currentPosition[0]+vector[0]*(randRoad)
        currY = currentPosition[1]+vector[1]*(randRoad)
        if currX >= self.width or currX <0 or currY >= self.height or currY <0:
                return

        # Call newIntersection to determine whether we should create a new intersection or not.
        if self.cityMap[currY][currX] == '.':
            self.newIntersection((currX,currY),direction)

    def newIntersection(self,currentPosition,direction):
        """This function decides whether to create a new intersection, straight road, or stop."""

        print("New intersection at: ", currentPosition, " in direction: ", direction)

        prob = random.randint(0,10)

        currX = currentPosition[0]
        currY = currentPosition[1]

        # 30% probability of a new intersection, 40% probabiloity of a straight road, 30% probability that the road just ends
        if prob < 6:
            # New intersection
            self.cityMap[currY][currX] = '+'

            # start a road in every direction except where we came from
            if (direction != 'u'):
                self.newRoad((currX,currY),'u')
            if (direction != 'd'):
                self.newRoad((currX,currY),'d')
            if (direction != 'l'):
                self.newRoad((currX,currY),'l')
            if (direction != 'r'):
                self.newRoad((currX,currY),'r')
        elif prob > 8:
            # Keep going
            if direction == 'u' or direction == 'd':
                self.cityMap[currentPosition[1]][currentPosition[0]] = '|'
            else:
                self.cityMap[currentPosition[1]][currentPosition[0]] = '-'

            self.newRoad((currX,currY),direction)
        else:
            # else - blank - stop
            self.cityMap[currentPosition[1]][currentPosition[0]] = 'b'


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
            ".": 10,
            "1": 3,
            "-": 1,
            "|": 1,
            "+": 1,
            "b": 1,
        }
        return costs[grid[y][x]]
    

    def _heuristic(self, a, b):
        # Manhattan distance on a square grid
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def pathfinding(self, grid, start, end):
        if not grid or not grid[0]:
            return []

        width = len(grid[0])
        height = len(grid)
        start = tuple(start)
        end = tuple(end)

        def is_inside(position):
            x, y = position
            return 0 <= x < width and 0 <= y < height

        if not is_inside(start) or not is_inside(end):
            return []

        frontier = []
        frontier.append([self._heuristic(start, end), 0, start])
        came_from = {start: None}
        cost_so_far = {start: 0}

        while frontier:
            frontier.sort(key=lambda item: item[0])
            best = frontier.pop(0)
            current_cost = best[1]
            current = best[2]

            if current == end:
                break

            if current_cost != cost_so_far[current]:
                continue

            for next_position in self._get_neighbors(grid, current):
                new_cost = current_cost + self._terrain_cost(grid, next_position)

                if next_position not in cost_so_far or new_cost < cost_so_far[next_position]:
                    cost_so_far[next_position] = new_cost
                    priority = new_cost + self._heuristic(next_position, end)
                    frontier.append([priority, new_cost, next_position])
                    came_from[next_position] = current

        if end not in came_from:
            return []

        path = []
        current = end
        while current is not None:
            path.append(current)
            current = came_from[current]

        return path[::-1]


def draw_everything(screen, startpoint, endpoint, city_map=None, pathfinder=None):
    """Draw everything on the screen."""
    path = []
    if city_map is not None and pathfinder is not None:
        path = pathfinder.pathfinding(
            city_map,
            (startpoint.x, startpoint.y),
            (endpoint.x, endpoint.y),
        )

    if city_map is not None:
        for y, row in enumerate(city_map):
            for x, road in enumerate(row):
                if road == ".":
                    pygame.draw.rect(screen, (0, 255, 0), (x * 10, y * 10, 10, 10))
                elif road == "-":
                    pygame.draw.rect(screen, (139, 69, 19), (x * 10, y * 10, 10, 10))
                elif road == "|":
                    pygame.draw.rect(screen, (0, 0, 255), (x * 10, y * 10, 10, 10))
                elif road in ("+", "b"):
                    pygame.draw.rect(screen, (255, 255, 0), (x * 10, y * 10, 10, 10))

    for x, y in path:
        pygame.draw.rect(screen, (255, 255, 255), (x * 10, y * 10, 10, 10))

    startpoint.draw(screen) # draw startpoint
    endpoint.draw(screen) # draw endpoint


def main():
    pygame.init()

    screen_size = (1920, 1080)

    screen = pygame.display.set_mode(screen_size)


    grid_size = (screen_size[0] // 10, screen_size[1] // 10)

    city = City(grid_size[0], grid_size[1])
    city_map = city.generateCity()

    print(city_map)

    pathfinder = Pathfinding(city_map)

    startpoint = Point((10, 45), (0, 255, 255))
    endpoint = Point((45, 20), (255, 0, 0))


    draw_everything(screen, startpoint, endpoint, city_map, pathfinder)

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

                draw_everything(screen, startpoint, endpoint, city_map, pathfinder)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    # regenerate grid
                    city_map = city.generateCity()

                    # recalc path
                    draw_everything(screen, startpoint, endpoint, city_map, pathfinder)
                    

        pygame.display.flip() # Refresh the screen so drawing appears

if __name__ == "__main__":
    main()