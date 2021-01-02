import pygame
from pygame import gfxdraw
PieceName0={0:"将",1:"士",2:"象",3:"馬",4:"車",5:"砲",6:"卒"}
PieceName1={0:"帥",1:"仕",2:"相",3:"傌",4:"俥 ",5:"炮",6:"兵"}

class Piece(pygame.sprite.Sprite):
    #->x |  y   0-7 index 
    #    v
    # 0 General  suai
    # 1 advisor shi 
    # 2 minister xiang
    # 3horse ma
    # 4 Chariot che
    # 5 cannoe 
    # 6 soldier
    # 0 red
    # 1 black

    def __init__(self,boardSurface,_type,playerType,initX,initY,size):
        super().__init__()
        self.cellSize=size
        self.image=pygame.Surface((self.cellSize,self.cellSize),pygame.SRCALPHA)
        self.type=_type
        self.playerType=playerType
        self.X=initX
        self.Y=initY
        self.selected=False
        self.font=pygame.font.SysFont("hiraginosansgbttc",40)
        self.empty = pygame.Color(0,0,0,0)
        
        if (playerType==0):
            self.text = self.font.render (PieceName0[_type], True, (255, 0, 0))
        else:
            self.text = self.font.render (PieceName1[_type], True, (0, 0, 0))
        self.textpos = self.text.get_rect ()  
        self.textpos.center = self.image.get_rect (). center
        self.image.blit(self.text,self.textpos)
        
        self.rect=self.image.get_rect(center=((self.X+1)*self.cellSize,(self.Y+1)*self.cellSize))
    def reDrawImage(self):
        self.image.fill(self.empty)
        self.image.blit(self.text,self.textpos)
    def draw(self,screen):
        if not self.selected:
            self.reDrawImage()
        else:
            pygame.draw.circle(self.image,(255,0,0), (self.cellSize// 2, self.cellSize// 2),25,1)
        screen.blit(self.image,self.rect)
    def select(self):
        self.selected=True
    def deselect(self):
        self.selected=False
        
    def update(self,newX,newY):
        self.X=newX
        self.Y=newY
        self.rect=self.image.get_rect(center=((self.X+1)*self.cellSize,(self.Y+1)*self.cellSize))
        #self.boardSurface.blit (self.image,self.rect)
        #self.rect.center=((self.X+1)*self.cellSize,(self.Y+1)*self.cellSize)
        #pos = self.PieceBackground.get_rect(center=((self.X+1)*self.cellSize,(self.Y+1)*self.cellSize))
        #gfxdraw.aacircle(self.PieceBackground, pos.center[0],pos.center[1],30,(255,0,0))
        #gfxdraw.filled_circle(self.PieceBackground, pos.center[0],pos.center[1],30,(255,0,0))
        #pygame.gfxdraw.filled_circle(self.PieceBackground, 3, 3, 2, (0, 255, 0))
        #self.boardSurface.blit (self.image,self.rect)
    def __str__(self):
        return str(self.type)+" "
    def is_clicked(self):
        return pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos())










