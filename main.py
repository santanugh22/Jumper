import pygame
import sys
from CONSTANTS import *
from utils import grid_maker
from level import Level




pygame.init()
clock=pygame.time.Clock()



screen=pygame.display.set_mode((WIDTH,HEIGHT))


# Background and the sun
sky=pygame.image.load('img/sky.png')
sky_bg=pygame.transform.scale(sky,(WIDTH,HEIGHT))
sky_rect=sky_bg.get_rect(topleft=(0,0))


sun_img=pygame.image.load('img/sun_shiny.png')

sun_rect=sun_img.get_rect(center=(100,100))

level=Level(LEVEL_DATA)








while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()


    

    screen.blit(sky_bg,sky_rect)
    screen.blit(sun_img,sun_rect)
    level.run(screen)


    # grid_maker(screen)

    pygame.display.update()
    clock.tick(60)

