import pygame
import math
from datetime import datetime

pygame.init()
screen = pygame.display.set_mode((640, 480))
screen.fill((255, 255, 255)) # Fill the screen with white

start_pos = (320, 240)

length = 200

x = 320
y = 240

amplitude = 180
dir = 1
spd = 0.03
clock = pygame.time.Clock()

start_pos_2 = ()
first_pos = ()

draw = True
list = []
new_list = []


run_flag = True
while run_flag is True:

    
    # Opgave 2
    """  s = datetime.now().second

    x_end = start_pos[0]  + length * math.cos(math.radians(s * 6-90)) 
    y_end = start_pos[1] + length * math.sin(math.radians(s * 6-90))

    pygame.draw.line(screen, (0,0,0,), start_pos, (x_end, y_end), 2) """

    # Opgave 4
    """ 
    dir += spd
    y = start_pos[1] - amplitude * math.sin(dir)
    
    pygame.draw.circle(screen, (0,0,0), (x,y), 5) """

    # Opgave 5 og 6
    """pressed = pygame.mouse.get_pressed()

    if pressed[0] == True:
        pos = pygame.mouse.get_pos()


        x = pos[0]
        y = pos[1]

        if 0 < x < 320 and 0 < y < 240:
            color = "cyan"
        elif 320 < x < 640 and 0 < y < 240:
            color = "magenta"
        elif 0 < x < 320 and 240 < y < 480:
            color = "yellow"
        elif 320 < x < 640 and 240 < y < 480:
            color = "black"

        pygame.draw.circle(screen, color, pos, 5) """

    # Opgave 7
    """pressed = pygame.mouse.get_pressed()


    if pressed[0] == True:
        pos = pygame.mouse.get_pos()

        if start_pos_2 != ():
            pygame.draw.line(screen, (0,0,0), start_pos_2, pos, 2)

        start_pos_2 = pos

        print(start_pos_2) """


    # Opgave 8
    # Opgave 8
    """     pressed = pygame.mouse.get_pressed()

    if pressed[0] == True:
        pos = pygame.mouse.get_pos()
        
        if not pos in new_list:
            new_list.append(pos)

        if len(new_list) > 1:
            if new_list[0][0] - 5 < pos[0] < new_list[0][0] + 5 or new_list[0][1] - 5 < pos[1] < new_list[0][1] + 5:
                print("jeg er meget tæt på")

                list.append(new_list)
                new_list = []

        print(new_list)
    for index in range(1, len(new_list)):
        pygame.draw.line(screen, (0, 0, 0), new_list[index - 1], new_list[index]) """
        
        

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_flag = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = event.pos

            if start_pos_2 == ():
                first_pos = pos

            if start_pos_2 != ():
                pygame.draw.line(screen, (0, 0, 0), start_pos_2, pos, 2)

            start_pos_2 = pos

            if first_pos != () and (
                first_pos[0] - 5 < pos[0] < first_pos[0] + 5
                and first_pos[1] - 5 < pos[1] < first_pos[1] + 5
            ):
                if first_pos != pos:
                    start_pos_2 = ()
                    first_pos = ()
                    print("Reset")

            print(start_pos_2, first_pos)

    pygame.display.flip() # Refresh the screen so drawing appears
    clock.tick(60)