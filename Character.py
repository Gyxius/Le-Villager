"""
The abstract class Character that the player and
other NPC will inherit from
"""
import pygame
from pygame.locals import *
from constants import *
from ImageLoader import *
import random

class Character(pygame.sprite.Sprite):
    """
    The abstract class that the player and enemies will inherit from

    Attributes
    ----------
    health : int
        The health of the character
    current_time : time
        The current time
    speed : int
        The character speed in milliseconds

    Methods
    -------
    movement_speed(func)
        Decorator which will enable a method to be executed x milliseconds
    """
    def __init__(self, health = 100):
        pygame.sprite.Sprite.__init__(self)
        self.health = health
        self.current_time = pygame.time.get_ticks()  # Get current time
        self.speed = 1000

    def attack(self):
        pass

    def defend(self):
        pass

    def move(self):
        pass

    def movement_speed(func):
        def inner(self):
            current_time = pygame.time.get_ticks()
            if current_time - self.current_time >= self.speed:
                func(self)
                self.current_time = current_time
        return inner

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

    def move(self, event):
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

class Enemy(Character):
    """
    A class that represents the enemies

    Attributes
    ----------
    image : surface
        The sprite of the player
    rect : tuple
        The rectangle surrounding the player
    enemy_changex: int
        The x position change
    enemy_changey: int
        The y position change 
    enemyx : int
        The X position of the player 
    enemyy : int
        The Y position of the player
    state: str
        The state of the enemy, either neutral or attacked
    speed : int
        The speed in milliseconds 

    Methods
    -------
    moveplayer(event)
        Moves the player on the x axis (so far)
    """
    def __init__(self):
        Character.__init__(self)
        self.image = Loader.load('img/skeleton.png', 'LEFT')
        self.rect = self.image.get_rect()
        self.enemy_changex = 0
        self.enemy_changey = 0
        self.enemyx = 7*TILE_SIZE
        self.enemyy = 7*TILE_SIZE
        self.rect.x = self.enemyx
        self.rect.y = self.enemyy
        self.state = "Neutral"
        self.speed = 1000

    @Character.movement_speed
    def move(self):
        """
        Change the position of the character
        The enemy either moves randomly if the state is "Neutral" or toward the player if "Attacked"
        """
        if self.state == "Neutral":
            self.enemy_changex = random.randint(-1,1)
            self.enemyx += self.enemy_changex*TILE_SIZE 
            if self.enemy_changex == 1:
                self.image = Loader.load('img/skeleton.png', 'RIGHT')
            elif self.enemy_changex == -1:
                self.image = Loader.load('img/skeleton.png', 'LEFT')
        if self.state == "Attacked":
            ## TODO update by adding the player, or actually using the group
            pass
                
    def update(self):
        self.move()
        self.rect.x  = self.enemyx
        self.rect.y  = self.enemyy

        
