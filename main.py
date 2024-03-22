import pygame
import sys
from pygame.locals import *
from constants import *
from Character import *

class Game:

    def __init__(self):
        pygame.init()
        self.WINDOW_WIDTH = 1280
        self.WINDOW_HEIGHT = 720
        self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.screen.fill(WHITE)
        pygame.display.set_caption('Le Villager')
        self.char = Character((0, 255, 0), 30, 30)
        self.character_group = pygame.sprite.Group()
        self.character_group.add(self.char)

    def update(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
                sys.exit()


    def draw(self):
        self.character_group.update()
        self.character_group.draw(self.screen)
        pygame.display.update()

    def gameLoop(self):
        while True:
            self.update()
            self.draw()


if __name__ == "__main__":
    game = Game()
    game.gameLoop()


    