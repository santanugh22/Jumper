import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self,screen,pos):
        self.screen=screen
        self.pos=pos
        