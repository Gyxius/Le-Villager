"""
The abstract class Character that the player and
other NPC will inherit from
"""
import pygame
from pygame.locals import *
from constants import *
from ImageLoader import *

class Character(pygame.sprite.Sprite):
    def __init__(self, health = 100):
        pygame.sprite.Sprite.__init__(self)
        self.health = health

    def attack(self):
        pass

    def defend(self):
        pass

class Player(Character):
    """
    A class that represents the main character

    Attributes
    ----------
    image : surface
        The sprite of the player
    rect : tuple
        The rectangle surrounding the player
    y : int
        The Y position of the player 
    x : int
        The X position of the player 
    name : string
        The name of the player

    Methods
    -------
    moveplayer(event)
        Moves the player on the x axis (so far)
    """
    def __init__(self, name = "Bob", pos_x = 0, pos_y = 0,):
        Character.__init__(self)
        self.image = Loader.load('img/knight.png', 'LEFT')
        self.rect = self.image.get_rect()
        self.playerx = pos_x*TILE_SIZE
        self.playery = pos_y*TILE_SIZE
        self.rect.x = self.playerx
        self.rect.y = self.playery
        self.name = name

    def movePlayer(self, event):
        if event.type == KEYDOWN:
            if event.key == K_q:
                self.playerx -= TILE_SIZE 
                self.image = Loader.load('img/knight.png', 'LEFT')
            elif event.key == K_d:
                self.playerx += TILE_SIZE 
                self.image = Loader.load('img/knight.png', 'RIGHT')

    def update(self):
        self.rect.x  = self.playerx
        self.rect.y  = self.playery
    
        


        
