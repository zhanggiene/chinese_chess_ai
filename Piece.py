import pygame
from pygame import gfxdraw
class Piece:
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
        self.cellSize=size
        self.type=_type
        self.playerType=playerType
        self.X=initX
        self.Y=initY
        self.font=pygame.font.SysFont("hiraginosansgbttc",40)
        self.PieceBackground=pygame.Surface((self.cellSize,self.cellSize),pygame.SRCALPHA)
        self.text = self.font.render ("将", True, (255, 255, 255)) # new image is create
        textpos = self.text.get_rect ()  
        textpos.center = self.PieceBackground.get_rect (). center
        self.PieceBackground.blit(self.text,textpos)
        self.boardSurface=boardSurface
        
        
    def draw(self):
        pos = self.PieceBackground.get_rect(center=(self.X*self.cellSize,self.Y*self.cellSize))
        #gfxdraw.aacircle(self.PieceBackground, pos.center[0],pos.center[1],30,(255,0,0))
        #gfxdraw.filled_circle(self.PieceBackground, pos.center[0],pos.center[1],30,(255,0,0))
        #pygame.gfxdraw.filled_circle(self.PieceBackground, 3, 3, 2, (0, 255, 0))
        self.boardSurface.blit (self.PieceBackground,pos)










