import pygame
import math

def draw_grid(rows, columns):
    row = []
    for x in range(rows):
        column = []

        row.append(column)
        for y in range(columns):
        
            column.append("0")

    return row


def grid_line(grid, start_coord, end_coord):
    start_x, start_y = start_coord
    end_x, end_y = end_coord


    new_grid = []
    for row in grid:
        new_grid.append(row.copy())

    if start_x != end_x and start_y != end_y:
        print("Line must be either horizontal or vertical")
        return

    if start_y == end_y:
        for x in range(start_x, end_x + 1):
            new_grid[start_y][x] = "1"
    else:
        for y in range(start_y, end_y + 1):
            new_grid[y][start_x] = "1"

    return new_grid

def draw_grid_on_screen(screen, grid):
    rows = len(grid)
    columns = len(grid[0])

    for x in range(rows):
        for y in range(columns):
            if grid[x][y] == "1":
                pygame.draw.rect(screen, (0, 0, 0), (y * 10, x * 10, 10, 10))
            else:
                pygame.draw.rect(screen, (255, 255, 255), (y * 10, x * 10, 10, 10))



def main():
    pygame.init() # Initialize Pygame
    screen = pygame.display.set_mode((640, 480)) # Create a window of 640x480 pixels

    grid = draw_grid(48, 64)

    grid = grid_line(grid, (0, 0), (0, 47))
    grid = grid_line(grid, (63, 0), (63, 47))
    grid = grid_line(grid, (2, 0), (63, 0))
    grid = grid_line(grid, (0, 47), (61, 47))

    grid = grid_line(grid, (1, 7), (57, 7))
    grid = grid_line(grid, (6, 15), (62, 15))
    grid = grid_line(grid, (1, 23), (57, 23))
    grid = grid_line(grid, (6, 31), (62, 31))
    grid = grid_line(grid, (1, 39), (57, 39))

    grid = grid_line(grid, (10, 1), (10, 5))
    grid = grid_line(grid, (22, 2), (22, 6))
    grid = grid_line(grid, (35, 1), (35, 4))
    grid = grid_line(grid, (48, 3), (48, 6))

    grid = grid_line(grid, (14, 8), (14, 12))
    grid = grid_line(grid, (28, 10), (28, 14))
    grid = grid_line(grid, (43, 8), (43, 12))
    grid = grid_line(grid, (55, 10), (55, 14))

    grid = grid_line(grid, (9, 17), (9, 22))
    grid = grid_line(grid, (23, 16), (23, 20))
    grid = grid_line(grid, (38, 18), (38, 22))
    grid = grid_line(grid, (51, 16), (51, 20))

    grid = grid_line(grid, (16, 24), (16, 29))
    grid = grid_line(grid, (31, 26), (31, 30))
    grid = grid_line(grid, (46, 24), (46, 28))
    grid = grid_line(grid, (57, 27), (57, 30))

    grid = grid_line(grid, (11, 33), (11, 38))
    grid = grid_line(grid, (26, 32), (26, 36))
    grid = grid_line(grid, (40, 34), (40, 38))
    grid = grid_line(grid, (53, 32), (53, 36))

    grid = grid_line(grid, (8, 41), (8, 45))
    grid = grid_line(grid, (20, 42), (20, 46))
    grid = grid_line(grid, (34, 40), (34, 44))
    grid = grid_line(grid, (47, 42), (47, 46))

    draw_grid_on_screen(screen, grid)

    run_flag = True
    while run_flag is True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_flag = False

        pygame.display.flip() # Refresh the screen so drawing appears


if __name__ == "__main__":
    main()
