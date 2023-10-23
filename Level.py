import pygame
from CONSTANTS import *

class Level:
    def __init__(self,level_data):


        for item,index in enumerate(level_data):
            if item==1:
                self.image=pygame.image.load('img/grass.png')
                self.rect=self.image.get_rect(center=(index*TILE_SIZE,index))


            else:
                continue


# this is teh false text that os being written in ithe main section of the page to be very awary of the situation of the main thing in the
        

        


        




