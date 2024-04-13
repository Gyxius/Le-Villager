import pygame
import sys
from pygame.locals import *
from constants import *
from character import *
from map import *

class Game:
    def __init__(self):
        pygame.init()
        self.WINDOW_WIDTH = TILE_SIZE*10
        self.WINDOW_HEIGHT = TILE_SIZE*10
        self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        pygame.display.set_caption('Le Villager')
        self.screen.fill(LIGHT_BLUE)
        self.map = Map()
        self.player1 = Player("Bob", 5, 7)
        self.enemy1 = Enemy()
        self.enemy_group = pygame.sprite.Group()
        self.enemy_group.add(self.enemy1)
        self.clock = pygame.time.Clock()

    def update(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
                sys.exit()
            else:
                self.player1.move(event)
            

    def draw(self):
        self.screen.fill(LIGHT_BLUE)
        self.map.drawGrid(self.screen)
        self.player1.update()
        self.player1.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        pygame.display.update()

    def gameLoop(self):
        while True:
            self.clock.tick(FPS)
            self.update()
            self.draw()
            if pygame.sprite.spritecollide(self.player1, self.enemy_group, False):
                print("collision detected")


if __name__ == "__main__":
    game = Game()
    game.gameLoop()


    