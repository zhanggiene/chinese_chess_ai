import pygame
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

    def __init__(self,_type,playerType,initX,initY):
        self.type=_type
        self.playerType=playerType
        self.X=initX
        self.Y=initY
        self.font=pygame.font.SysFont("hiraginosansgbttc",50)
    def draw(self):
        





