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

    def getGrid(self):
        """
        Returns the Grid
        """
        return self.grid
    
    def draw(self, screen, WINDOW_WIDTH, WINDOW_HEIGHT):
        """
        Draw the Background colors and the grid
        """
        screen.fill(LIGHT_BLUE)
        pygame.draw.rect(screen, GRASS_GREEN, (TILE_SIZE*0, TILE_SIZE*7, WINDOW_WIDTH * TILE_SIZE, WINDOW_HEIGHT * TILE_SIZE))
        #self.drawGrid(screen)


if __name__ == "__main__":
    map = Map()
    map.createGrid()
    map.printGrid()





