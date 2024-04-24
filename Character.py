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

    def move(self):
        pass

    def movement_speed(func):
        def inner(self, player):
            current_time = pygame.time.get_ticks()
            if current_time - self.current_time >= self.speed:
                func(self, player)
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
    def __init__(self, group, name = "Bob", pos_x = 0, pos_y = 0):
        Character.__init__(self)
        self.spritetype = "player" 
        self.image = Loader.load('img/knight.png', 'LEFT')
        self.rect = self.image.get_rect()
        self.playerx = pos_x*TILE_SIZE
        self.playery = pos_y*TILE_SIZE
        self.playerdx = 0
        self.playerdy = 0
        self.rect.x = self.playerx
        self.rect.y = self.playery
        self.name = name
        self.group = group
        self.health = 100
        self.attack = 30

    def move(self, event):
        if event.key == K_q:
            self.playerdx = -TILE_SIZE
        elif event.key == K_d:
            self.playerdx = TILE_SIZE 
        
        if self.playerdx < 0:
            self.image = Loader.load('img/knight.png', 'LEFT')
        elif self.playerdx > 0:
            self.image = Loader.load('img/knight.png', 'RIGHT')
        else:
            pass
        self.checkCollision()
        self.playerx += self.playerdx 
        self.playerdx = 0

    def update(self):
        self.rect.x  = self.playerx
        self.rect.y  = self.playery

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        print("draw")

    def checkCollision(self):
        requested_rect = pygame.Rect.copy(self.rect)
        requested_rect.x += self.playerdx
        for sprite in self.group:
            if sprite.rect.colliderect(requested_rect):
                self.playerdx = 0
    
    def getDamage(self, enemy):
        # Get vulnerability
        self.health -= enemy.attack


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
    def __init__(self, group):
        Character.__init__(self)
        self.spritetype = "enemy" 
        self.image = Loader.load('img/skeleton.png', 'LEFT')
        self.rect = self.image.get_rect()
        self.enemyx = 7*TILE_SIZE
        self.enemyy = 7*TILE_SIZE
        self.enemydx = 0
        self.enemydy = 0
        self.rect.x = self.enemyx
        self.rect.y = self.enemyy
        self.state = "Idle"
        self.speed = 1000 #in ms
        self.group = group
        self.health = 100
        self.attack = 10

    @Character.movement_speed
    def move(self, player):
        """
        Change the position of the character
        The enemy either moves randomly if the state is "Neutral" or toward the player if "Attacked"
        """
        if self.state == "Idle":
            self.enemydx = random.randint(-1,1) * TILE_SIZE 

        elif self.state == "Attacked":
            self.enemydx = self.follow(player) * TILE_SIZE 
        
        if self.enemydx > 0:
            self.image = Loader.load('img/skeleton.png', 'RIGHT')
        elif self.enemydx < 0:
            self.image = Loader.load('img/skeleton.png', 'LEFT')
        else:
            if self.state == "Attacked":
                player.getDamage(self)

        self.checkCollision()
        self.enemyx += self.enemydx 
        self.enemydx = 0

    def checkCollision(self):
        requested_rect = pygame.Rect.copy(self.rect)
        requested_rect.x += self.enemydx
        for sprite in self.group:
            if sprite.rect.colliderect(requested_rect):
                self.enemydx = 0
    
    def follow(self, player):
        if player.playerx <= self.enemyx <= player.playerx + TILE_SIZE:
            return 0
        elif player.playerx < self.enemyx  :
            return -1
        elif player.playerx > self.enemyx  :
            return 1
        else:
            return 0
    
    def getDamage(self, player):
        # Get vulnerability
        if self.state == "Idle":
            self.state = "Attacked"
        self.health -= player.attack

    def checkDeath(self):
        if self.health < 0:
            self.kill()
        
    def update(self):
        self.rect.x  = self.enemyx
        self.rect.y  = self.enemyy
        self.checkDeath()

        
