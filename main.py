# Begining of the game code

import pygame
import sys
from CONSTANTS import *
from Level import Level

pygame.init()
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock=pygame.time.Clock()
pygame.display.set_caption("Meow")
sun_image=pygame.image.load('./img/sun_shiny.png').get_alpha()
sun_rect=sun_image.get_rect(center=(200,200))


sky_bg=pygame.image.load('./img/sky.png')
sky_rect=sky_bg.get_rect(topleft=(0,0))
level_map=Level(level_data)



def draw_grid():
    for line in range(0,10):
        pygame.draw.line(screen,'black',(0,line*TILE_SIZE),(SCREEN_WIDTH,line*TILE_SIZE))
        pygame.draw.line(screen,'black',(TILE_SIZE*line,0),(TILE_SIZE*line,SCREEN_HEIGHT))


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
            pygame.quit()

   
   
    screen.blit(sky_bg,sky_rect)
    screen.blit(sun_image,sun_rect)
    screen.blit()
    draw_grid()

    


    pygame.display.update()
    clock.tick(60)
    
    
        
