import pygame
import math
import time

pygame.init() # Initialize Pygame
screen = pygame.display.set_mode((640, 480)) # Create a window of 640x480 pixels

clock = pygame.time.Clock()
dt = 0


run_flag = True
while run_flag is True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_flag = False

    rm = time.localtime()



    hour_degree = (rm.tm_hour) * 30 - 90
    minute_degree = rm.tm_min * 6 - 90
    second_degree = rm.tm_sec * 6 - 90

    screen.fill((255, 255, 255)) # Fill the screen with white

    pygame.draw.circle(screen, (0,0,0,), (320, 240), 175, 2)
        
    hour_length = 175 # Set the length of the line
    hour_length_2 = 25 # Set the length of the line

    x_middle = 320
    y_middle = 240

    hour_x_start = x_middle + hour_length * math.cos(math.radians(hour_degree)) 
    hour_y_start = y_middle + hour_length * math.sin(math.radians(hour_degree))


    hour_x_end = hour_x_start + hour_length_2 * math.cos(math.radians(hour_degree)) 
    hour_y_end = hour_y_start + hour_length_2 * math.sin(math.radians(hour_degree))

    pygame.draw.line(screen, (0,0,0,), (hour_x_start, hour_y_start), (hour_x_end, hour_y_end), 6)


    minute_length = 175 # Set the length of the line
    minute_length_2 = 25

    minute_x_start = x_middle + minute_length * math.cos(math.radians(minute_degree)) 
    minute_y_start = y_middle + minute_length * math.sin(math.radians(minute_degree))

    minute_x_end = minute_x_start + minute_length_2 * math.cos(math.radians(minute_degree)) 
    minute_y_end = minute_y_start + minute_length_2 * math.sin(math.radians(minute_degree))

    pygame.draw.line(screen, (0,0,0,), (minute_x_start, minute_y_start), (minute_x_end, minute_y_end), 4)


    second_length = 175 # Set the length of the line
    second_length_2 = 25 # Set the length of the line

    second_x_start = x_middle + second_length * math.cos(math.radians(second_degree)) 
    second_y_start = y_middle + second_length * math.sin(math.radians(second_degree))

    second_x_end = second_x_start + second_length_2 * math.cos(math.radians(second_degree)) 
    second_y_end = second_y_start + second_length_2 * math.sin(math.radians(second_degree))

    pygame.draw.line(screen, (0,0,0,), (second_x_start, second_y_start), (second_x_end, second_y_end), 2)

    for i in range(12): # Loop to draw 12 lines

        turn_angle = 30 # Set the rotation angle increment

        degree = i * turn_angle - 90 # Initialize the rotation angle

        length = 150 # Set the length of the line
        length_2 = 25 # Set the length of the line

        x_middle = 320 
        y_middle = 240

        x_start = x_middle + length * math.cos(math.radians(degree)) 
        y_start = y_middle + length * math.sin(math.radians(degree))

        x_end = x_start + length_2 * math.cos(math.radians(degree)) 
        y_end = y_start + length_2 * math.sin(math.radians(degree))

        pygame.draw.line(screen, (0,0,0,), (x_start, y_start), (x_end, y_end), 2) # Draw a line from the center to the calculated end point


    pygame.display.flip() # Refresh the screen so drawing appears