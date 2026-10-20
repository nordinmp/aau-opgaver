import pygame
import random

pygame.init()
screen = pygame.display.set_mode((640, 480))

hori_move = 0
vert_move = 0

box_pos = (100,100)
box_size = (25,25)
clock = pygame.time.Clock()

golds = []

player_point = 0

def spawn_gold():
    x = random.randint(50, 590)
    y = random.randint(50, 430)
    
    point = random.randint(1,100)

    rad = 5 * point/100 

    gold = {
        "x" : x,
        "y" : y,
        "radius": rad,
        "point": point
    }

    golds.append(gold)

for i in range(15):
    spawn_gold()


run_flag = True
while run_flag is True:
    screen.fill((0, 0, 0)) # Fill the screen with white

    rect = box_pos + box_size

    pygame.draw.rect(screen, "white", rect)

    for gold in golds:
        pos = (gold["x"], gold["y"])
        pygame.draw.circle(screen, "yellow", pos, gold["radius"] )


        a = pos[1] - box_pos[1]
        b = pos[0] - box_pos[0]

        c = (a**2 + b**2)**0.5

        if c <= box_size[0]:
            print("fjernet")
            print(gold)

            player_point += gold["point"]


            print(player_point)

            golds.remove(gold)

    if len(golds) <= 10:
        spawn_gold()



    # print points
    font = pygame.font.Font(None, 36)
    text = font.render(f"Points: {player_point}", True, (0, 0, 0))
    screen.blit(text, (10, 10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_flag = False

        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_w, pygame.K_UP):
                hori_move = -5
                vert_move = 0
            if event.key in (pygame.K_s, pygame.K_DOWN):
                hori_move = 5
                vert_move = 0
            if event.key in (pygame.K_a, pygame.K_LEFT):
                vert_move = -5
                hori_move = 0
            if event.key in (pygame.K_d, pygame.K_RIGHT):
                vert_move = 5
                hori_move = 0

    box_pos = box_pos[0] + vert_move, box_pos[1] + hori_move

    # venstre
    if box_pos[0] <= 0:
        box_pos = 639 - box_size[0], box_pos[1]
        print("venstre")

    # højre
    if box_pos[0] >= 640:
        box_pos = 0 + box_size[0], box_pos[1]
        print("højre")

    # up
    if box_pos[1] <= 0:
        box_pos = box_pos[0], 480 - box_size[1]
        print("up")

    # ned
    if box_pos[1] >= 479:
        box_pos = box_pos[0], 0 + box_size[1]
        print("ned")

    pygame.display.flip() # Refresh the screen so drawing appears
    clock.tick(60)
