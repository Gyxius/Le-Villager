from constants import *

class Loader():
    """
    A class used to represent the sprite loader

    Attributes
    ----------
    img_size : int
        a string that represents the surface we want inside the image

    Methods
    -------
    load(path=None)
        Returns the image
    """
    img_size = 119
    @staticmethod
    def load(path):
        """
        Given an image path, it returns the image
        The image returned will be used by the character class

        Args:
            path (string): the path of the image file

        Returns 
            image: The image to be loaded for the character image attribute    
        """
        cropped_image = (0*Loader.img_size, 1*Loader.img_size, Loader.img_size, Loader.img_size)
        image = pygame.image.load(path).subsurface(cropped_image)
        image  = pygame.transform.scale(image , (TILE_SIZE, TILE_SIZE))
        return image 


