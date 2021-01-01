import pygame
from pygame import gfxdraw
PieceName0={0:"将",1:"士",2:"象",3:"馬",4:"車",5:"砲",6:"卒"}
PieceName1={0:"帥",1:"仕",2:"相",3:"傌",4:"俥 ",5:"炮",6:"兵"}
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
        if (playerType==0):
            self.text = self.font.render (PieceName0[_type], True, (255, 0, 0))
        else:
            self.text = self.font.render (PieceName1[_type], True, (0, 0, 0))
        textpos = self.text.get_rect ()  
        textpos.center = self.PieceBackground.get_rect (). center
        self.PieceBackground.blit(self.text,textpos)
        self.boardSurface=boardSurface
    
        
        
    def draw(self):
        pos = self.PieceBackground.get_rect(center=((self.X+1)*self.cellSize,(self.Y+1)*self.cellSize))
        #gfxdraw.aacircle(self.PieceBackground, pos.center[0],pos.center[1],30,(255,0,0))
        #gfxdraw.filled_circle(self.PieceBackground, pos.center[0],pos.center[1],30,(255,0,0))
        #pygame.gfxdraw.filled_circle(self.PieceBackground, 3, 3, 2, (0, 255, 0))
        self.boardSurface.blit (self.PieceBackground,pos)
    def __str__(self):
        return str(self.type)+" "










