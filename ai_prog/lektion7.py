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

    grid = grid_line(grid, (0, 0), (0, 3))



    draw_grid_on_screen(screen, grid)

    run_flag = True
    while run_flag is True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_flag = False

        pygame.display.flip() # Refresh the screen so drawing appears


if __name__ == "__main__":
    main()
