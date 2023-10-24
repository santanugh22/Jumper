import pygame
from CONSTANTS import *
color='white'
def grid_maker(surface):
    for index in range(20):
        pygame.draw.line(surface,color,(index*TILE_SIZE,0),(index*TILE_SIZE,HEIGHT))
        pygame.draw.line(surface,color,(0,index*TILE_SIZE),(WIDTH,index*TILE_SIZE))

