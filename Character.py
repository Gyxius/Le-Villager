"""
The abstract class Character that the player and
other NPC will inherit from
"""
import pygame
from pygame.locals import *
from constants import *

class Character(pygame.sprite.Sprite):
    def __init__(self, health = 100):
        pygame.sprite.Sprite.__init__(self)
        self.health = health

    def attack(self):
        pass

    def defend(self):
        pass

class Player(Character):
    def __init__(self, name = "Bob", pos_x = 0, pos_y = 0,):
        Character.__init__(self)
        IMG_SIZE = 119
        self.cropped_region = (0*IMG_SIZE, 1*IMG_SIZE, IMG_SIZE, IMG_SIZE)
        self.image = pygame.image.load('img/knight.png').subsurface(self.cropped_region)
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect()
        self.x = pos_x*TILE_SIZE
        self.y = pos_y*TILE_SIZE
        self.rect.x = self.x
        self.rect.y = self.y
        self.name = name

    def movePlayer(self, event):
        if event.type == KEYDOWN:
            if event.key == K_q:
                self.rect.x -= TILE_SIZE
            elif event.key == K_d:
                self.rect.x += TILE_SIZE

    
        


        
