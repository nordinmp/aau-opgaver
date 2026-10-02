import pygame
import math
start_pos = (100, 100)
box_size = (25, 25)
screen = pygame.display.set_mode((640, 480))
screen.fill((255, 255, 255)) # Fill the screen with white

#OPGAVE 1
""" for i in range(10):
    pos = (start_pos[0] + i * box_size[0] * 2, start_pos[1])
    pygame.draw.rect(screen, (0, 0, 0), (pos, box_size)) """

# OPGAVE 2
""" for i in range(12):
    turn_angle = 30 # Set the rotation angle increment

    degree = i * turn_angle

    length = 150 # Set the length of the line

    x_start = 320 
    y_start = 240

    x_end = x_start + length * math.cos(math.radians(degree)) 
    y_end = y_start + length * math.sin(math.radians(degree))

    pygame.draw.line(screen, (0,0,0,), (x_start, y_start), (x_end, y_end), 2) """


#OPGAVE 3
""" start_pos = (50, 50)
for i in range(4):
    for j in range(4):
        pos = (start_pos[0] + i * box_size[0] * 2, start_pos[1] + j * box_size[1] * 2)
        pygame.draw.rect(screen, (0, 0, 0), (pos, box_size))
        
    for j in range(4):
        pos = ((start_pos[0] + i * box_size[0] * 2) - 25, (start_pos[1] + j * box_size[1] * 2) - 25)
        pygame.draw.rect(screen, (0, 0, 0), (pos, box_size)) """


# OPGAVE 4
""" box_size = 1
start_pos = (1, 1)
x = start_pos[0]
y = start_pos[1]

for i in range(60):
    x += box_size
    y += box_size

    box_size += 1

    pygame.draw.rect(screen, (0, 0, 0), (x, y, box_size, box_size))
 """


start_pos = (320, 240)
box_size = (5,5)
# OPGAVE 5
for angle in range(0, 360 * 4, 5):
    r = 0.1 * angle

    x = start_pos[0] + r*math.cos(math.radians(angle)) * box_size[0]/4
    y = start_pos[1] + r*math.sin(math.radians(angle)) * box_size[1]/4

    pos = (x,y)

    pygame.draw.rect(screen, (0, 0, 0), (pos, box_size))



run_flag = True
while run_flag is True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_flag = False

    pygame.display.flip() # Refresh the screen so drawing appears