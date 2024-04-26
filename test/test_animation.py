import pygame
from pygame.locals import *
from constants import *

class Game:
    def __init__(self):
        pygame.init()
        self.WINDOW_WIDTH = 20
        self.WINDOW_HEIGHT = 10
        self.screen = pygame.display.set_mode((self.WINDOW_WIDTH * TILE_SIZE, self.WINDOW_HEIGHT * TILE_SIZE))
        pygame.display.set_caption('Le Villager')
        self.screen.fill(LIGHT_BLUE)
        x = 2
        y = 0
        size = 180
        cropped_image = (x*size, y*size, size, size)
        self.image = pygame.image.load('img/hit_animation.png').subsurface(cropped_image)
        self.image  = pygame.transform.scale(self.image , (TILE_SIZE, TILE_SIZE))

    def draw(self):
        self.screen.fill(LIGHT_BLUE)
        self.screen.blit(self.image, self.image.get_rect())
        pygame.display.update()
        

    def gameLoop(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.draw()

if __name__ == "__main__":
    game = Game()
    game.gameLoop()


    