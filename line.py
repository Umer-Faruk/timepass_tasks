import pygame
import random
import time

pygame.init()

dis= pygame.display.set_mode((1000,600))
pygame.display.set_caption("line")

class Line_class():
     def __init__(self,x,y,color):
          self.ax = 50
          self.ay= 50

          self.bx = x
          self.by = y

          self.color=color

     def drowline(self,dis,mx,my):
          self.ax = mx
          self.ay = my
          pygame.draw.line(dis,self.color,(self.bx,self.by),(self.ax,self.ay))


def main():
     over = True
     x=50
     y=50
     lins =[]
     

     for i in range(10):
         
          for j in range(10):
               r= random.randrange(255)
               g = random.randrange(255)
               b = random.randrange(255)
               
               l = Line_class(x,y,(r,g,b))
               lins.append(l)
               x += 100
          x = 50
          y += 50
          #
          

     mx = 0
     my = 0
     # print(lins)
     while over :
          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    over = False

          mx , my = pygame.mouse.get_pos()   
          # print(mx,my)
          # if mx <= 200 and my <= 200:
          for i in lins:
               if not pygame.mouse.get_focused():
                    i.drowline(dis,i.bx,i.by)
               
               else:

                    i.drowline(dis,mx,my)

          pygame.display.update()
          dis.fill((0,0,0))
         

     pygame.quit()
     quit()

main()
