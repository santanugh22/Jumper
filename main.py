import pygame
import sys
from CONSTANTS import *
from utils import grid_maker
from level import Level
from player import Player




pygame.init()
clock=pygame.time.Clock()



screen=pygame.display.set_mode((WIDTH,HEIGHT))


# Background and the sun
sky=pygame.image.load('img/sky.png')
sky_bg=pygame.transform.scale(sky,(WIDTH,HEIGHT))
sky_rect=sky_bg.get_rect(topleft=(0,0))


sun=pygame.image.load('img/sun_shiny.png')
sun_image=pygame.transform.scale(sun,(TILE_SIZE,TILE_SIZE))

sun_rect=sun_image.get_rect(center=(100,100))

level=Level(LEVEL_DATA)
player=Player(100,370)








while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()


    

    screen.blit(sky_bg,sky_rect)
    screen.blit(sun_image,sun_rect)
    
    level.run(screen)
    player.run(screen)


    # grid_maker(screen)

    pygame.display.update()
    clock.tick(60)

