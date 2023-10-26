import pygame
from CONSTANTS import *


class Level:
    def __init__(self, level_data) -> None:
        dirt_image = pygame.image.load('img/dirt.png')
        grass_image=pygame.image.load('img/grass.png')
        self.tiles = []

        row_count = 0
        for row in level_data:
            col_count = 0
            for tile in row:
                if tile == 0:
                    image = pygame.transform.scale(
                        dirt_image, (TILE_SIZE, TILE_SIZE))
                    rect = image.get_rect()
                    rect.x = col_count*TILE_SIZE
                    rect.y = row_count*TILE_SIZE
                    tile = (image, rect)
                    self.tiles.append(tile)
                if tile==2:
                      image = pygame.transform.scale(
                      grass_image, (TILE_SIZE, TILE_SIZE))
                      rect = image.get_rect()
                      rect.x = col_count*TILE_SIZE
                      rect.y = row_count*TILE_SIZE
                      tile = (image, rect)
                      self.tiles.append(tile)

                col_count+=1
            row_count+=1
       

    def run(self, screen):
        for tile in self.tiles:
            screen.blit(tile[0], tile[1])
            pygame.draw.rect(screen,(255,255,255),tile[1],2)
