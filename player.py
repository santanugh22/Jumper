import pygame
from CONSTANTS import *
from random import randint




class Player:
    def __init__(self,x,y) -> None:
      self.right_images=[]
      for i in range(1,5):
         image=pygame.image.load(f'img/guy{i}.png')
         image=pygame.transform.scale(image,(40,80))
         self.right_images.append(image)

      self.left_images=[]
      for i in range(1,5):
         image=pygame.image.load(f'img/guy{i}.png')
         image=pygame.transform.scale(image,(40,80))
         image=pygame.transform.flip(image,True,False)
         self.left_images.append(image)


      self.image=self.right_images[0]
      self.rect=self.image.get_rect(center=(x,y))
      self.y=y
      self.x=x
    
      self.gravity= 4
      self.jumped=False
      self.walk=False
      self.direction='Right'

    

    def movement(self):
       keys=pygame.key.get_pressed()

       if keys[pygame.K_RIGHT]:
          self.walk=True
          self.rect.x+=4
          self.direction='Right'

       if keys[pygame.K_LEFT]:
          self.walk=True
          self.rect.x-=5
          self.direction='Left'

       if keys[pygame.K_SPACE] and self.rect.y==self.y:

          self.rect.bottom-=200
          self.walk=False
          self.jumped=True

       if keys[pygame.K_LEFT]==False and keys[pygame.K_RIGHT]==False:
          self.walk=False

     
           
       


          
  
          
          
    def Animations(self):
         if self.walk==False and self.jumped==False:
              if self.direction=='Right':
                self.image=self.right_images[2]
              elif self.direction=='Left':
                 self.image=self.left_images[2]

         if self.walk==True:
          if self.direction=='Right':
             self.image=self.right_images[randint(0,3)]
          elif self.direction=='Left':
             self.image=self.left_images[randint(0,3)]
         if self.jumped==True:
          if self.direction=='Right':
             self.image=self.right_images[3]
          elif self.direction=='Left':
             self.image=self.left_images[3]
       
    
    def Gravity(self):
       if self.rect.y<self.y:
          self.rect.y+=self.gravity
       if self.rect.y>self.y:
            self.rect.y=self.y
       if self.rect.y==self.y:
          self.jumped=False

          
       
       
    
   

          




   
          
          

       
          
       


          
    


    def run(self,screen):
       self.movement()
       self.Animations()

       self.Gravity()

       
       
       
       
       screen.blit(self.image,self.rect)