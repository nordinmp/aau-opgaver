import pygame
import math

pygame.init() # Initialize Pygame
screen = pygame.display.set_mode((640, 480)) # Create a window of 640x480 pixels

clock = pygame.time.Clock()
dt = 0

degree = 0 # Initialize the rotation angle

run_flag = True
while run_flag is True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_flag = False

    screen.fill((255, 255, 255)) # Fill the screen with white

    for i in range(12): # Loop to draw 12 lines

        turn_angle = 30 # Set the rotation angle increment

        degree += turn_angle # Initialize the rotation angle

        length = 200 # Set the length of the line

        x_start = 320 
        y_start = 240

        x_end = x_start + length * math.cos(math.radians(degree)) 
        y_end = y_start + length * math.sin(math.radians(degree))

        pygame.draw.line(screen, (0,0,0,), (x_start, y_start), (x_end, y_end), 2) # Draw a line from the center to the calculated end point

    degree += 2 * dt

    dt = clock.tick(60)

    pygame.display.flip() # Refresh the screen so drawing appears