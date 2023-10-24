import pygame
from CONSTANTS import *




class Player:
    def __init__(self,x,y) -> None:
      image=pygame.image.load('img/guy1.png')
      self.image=pygame.transform.scale(image,(40,80))
      self.rect=self.image.get_rect()
      self.y=y
      self.rect.x=x
      self.rect.y=y
      self.gravity=9.8
    

    def movement(self):
       keys=pygame.key.get_pressed()

       if keys[pygame.K_RIGHT]:
          self.rect.x+=4
       if keys[pygame.K_LEFT]:
          self.rect.x-=5

       if keys[pygame.K_SPACE]:
          self.rect.y-=10

          




   
          
          

       
          
       


          
    


    def run(self,screen):
       self.movement()
       
       screen.blit(self.image,self.rect)