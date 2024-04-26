from constants import *

class Loader():
    """
    A class used to represent the sprite loader

    Attributes
    ----------
    img_tile : int
        the number of pixels for the tile size in each sprite within the image 

    Methods
    -------
    load(path=None)
        Returns the image
    """
    img_tile = 115 # px
    
    @staticmethod
    def load(path, direction):
        """
        Given an image path and a direction, it returns the sprite from the image 
        The image returned will be used by the character class
        The knight image has as dimension 3X3 with [0,0] being the top left part

        Args:
            path (string): the path of the image file
            direction (string) : left right depending on the position of the player

        Returns 
            image: The image to be loaded for the character image attribute    
        """
        direction_to_pixels= {'LEFT' : [0,1], 'RIGHT' : [2,1]}
        pixels_width = direction_to_pixels[direction][0]
        pixels_height = direction_to_pixels[direction][1]
        cropped_image = (pixels_width*Loader.img_tile, pixels_height*Loader.img_tile, Loader.img_tile, Loader.img_tile)
        image = pygame.image.load(path).subsurface(cropped_image)
        image  = pygame.transform.scale(image , (TILE_SIZE, TILE_SIZE))
        return image 


