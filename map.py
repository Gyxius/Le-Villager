import pygame
from constants import *

class Map:
    def __init__(self, HEIGHT = 10, WIDTH = 10):
        self.HEIGHT = HEIGHT
        self.WIDTH = WIDTH
        self.grid = []
        self.createGrid()
    
    def createGrid(self):
        """
        Create HEIGHT * WIDTH grid
        For example:
        [[" "," "," "],
         [" "," "," "],
         [" "," "," "]]
        """
    
        for i in range(self.WIDTH):
            row = []
            self.grid.append(row)
            for j in range(self.HEIGHT):
                self.grid[i] += " "

    def printGrid(self):
        """
        Print the grid to the terminal
        """
        for i in range(self.WIDTH):
            print("[", end = "")
            for j in range(self.HEIGHT):
                self.grid[i] += " "
                print(" ,", end = "")
            print("]")

    def drawGrid(self, screen):
        """
        Display the grid on the game
        """
        for x in range(self.WIDTH):
            for y in range(self.HEIGHT):
                rect = pygame.Rect(TILE_SIZE*x,TILE_SIZE*y, TILE_SIZE, TILE_SIZE)
                pygame.draw.rect(screen, WHITE, rect, 1)

if __name__ == "__main__":
    map = Map()
    map.createGrid()
    map.printGrid()





