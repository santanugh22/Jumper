# Begining of the game code

import pygame
import sys
from CONSTANTS import *

pygame.init()
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
            pygame.quit()
    screen.fill('yellow')
    pygame.display.set_caption("Meow")
        
