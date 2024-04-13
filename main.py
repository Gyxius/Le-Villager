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
        self.character_group = pygame.sprite.Group()
        self.attackable_group = pygame.sprite.Group()

        self.player1 = Player(self.character_group, "Bob", 5, 7)
        self.enemy1 = Enemy(self.character_group)
        self.attackable_group.add(self.enemy1)
        self.character_group.add(self.enemy1)
        self.character_group.add(self.player1)
        self.clock = pygame.time.Clock()

    def update(self):
        self.playerUpdate()
        self.enemyUpdate()
        self.character_group.update()

    def playerUpdate(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_q or event.key == K_d:
                    self.player1.move(event)
                if event.key == K_SPACE:
                    self.playerAttack()
        
    def playerAttack(self):
        """ Check if enemy is nearby and attacks it"""
        left_rect = pygame.Rect.copy(self.player1.rect)
        left_rect.x -= TILE_SIZE
        right_rect = pygame.Rect.copy(self.player1.rect)
        right_rect.x += TILE_SIZE
        for target_sprite in self.attackable_group:
            if target_sprite.rect.colliderect(left_rect) or target_sprite.rect.colliderect(right_rect):
                target_sprite.getDamage(self.player1)

    def enemyUpdate(self):
        #TODO use attackble group and update this group instead
        self.enemy1.move(self.player1)

    def draw(self):
        self.screen.fill(LIGHT_BLUE)
        self.map.drawGrid(self.screen)
        self.character_group.draw(self.screen)
        pygame.display.update()

    def gameLoop(self):
        while True:
            self.clock.tick(FPS)
            self.update()
            self.draw()

if __name__ == "__main__":
    game = Game()
    game.gameLoop()


    