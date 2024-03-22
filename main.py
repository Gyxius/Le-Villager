import pygame
import sys
from pygame.locals import *
from constants import *

class Game:

    def __init__(self):
        pygame.init()
        self.WINDOW_WIDTH = 1280
        self.WINDOW_HEIGHT = 720
        self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.screen.fill(WHITE)
        pygame.display.set_caption('Le Villager')

    def update(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


    def draw(self):
        pygame.display.update()

    def gameLoop(self):
        while True:
            self.update()
            self.draw()


if __name__ == "__main__":
    game = Game()
    game.gameLoop()


    