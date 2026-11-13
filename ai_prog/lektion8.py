import random

import pygame
from sklearn.neighbors import KNeighborsClassifier


class DataPoint:
    def __init__(self, x, y, label, color):
        self.x = x
        self.y = y
        self.label = label
        self.color = color

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), 5)


def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 400))

    fish_data = []

    for i in range(10):
        _x = random.gauss(200, 20)
        _y = random.gauss(200, 20)

        data_point = DataPoint(x=_x, y=_y, label="salmon", color="blue")
        data_point.draw(screen)

        fish_data.append(data_point)

    for i in range(10):
        _x = random.gauss(400, 20)
        _y = random.gauss(200, 20)

        data_point = DataPoint(x=_x, y=_y, label="seabass", color="red")
        data_point.draw(screen)

        fish_data.append(data_point)

    data_point_guess = DataPoint(x=240, y=150, label=None, color="green")
    data_point_guess.draw(screen)


    X = [[point.x, point.y] for point in fish_data]
    y = [point.label for point in fish_data]

    knn = KNeighborsClassifier(n_neighbors=3)

    knn.fit(X, y)

    x_test = [[data_point_guess.x, data_point_guess.y]]


    y_pred = knn.predict(x_test)

    print(f"Predicted label for the guess point: {y_pred[0]}")


    run_flag = True
    while run_flag is True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_flag = False

        pygame.display.flip() # Refresh the screen so drawing appears



if __name__ == "__main__":
    main()