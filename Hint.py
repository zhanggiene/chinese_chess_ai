import pygame
from pygame import gfxdraw
class Hint (pygame.sprite.Sprite):
    def __init__(self,boardSurface,initX,initY,size):
        super().__init__()
        self.cellSize=size  #control the position
        self.image=pygame.Surface((self.cellSize,self.cellSize),pygame.SRCALPHA)
        self.X=initX
        self.Y=initY
        self.show=False
        self.empty = pygame.Color(0,0,0,0)
        self.color=(0,0,255)
        self.rect=self.image.get_rect(center=((self.X+1)*self.cellSize,(self.Y+1)*self.cellSize))
    def draw(self,screen):
        if not self.show:
            self.image.fill(self.empty)
        else:
            #pygame.draw.circle(self.image,(255,0,0), (self.cellSize// 2, self.cellSize// 2),25,1)
            gfxdraw.filled_circle(self.image, self.cellSize// 2, self.cellSize// 2, 10,self.color)

        screen.blit(self.image,self.rect)
    def switchOn(self):
        self.show=True
    def switchOff(self):
        self.show=False
    def getShow(self):
        return self.show
    def is_clicked(self,pos):
        return self.rect.collidepoint(pos)
    



