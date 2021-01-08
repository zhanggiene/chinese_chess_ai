import pygame
from pygame import gfxdraw
PieceName0={0:"将",1:"士",2:"象",3:"馬",4:"車",5:"砲",6:"卒"}
PieceName1={0:"帥",1:"仕",2:"相",3:"傌",4:"俥 ",5:"炮",6:"兵"}
potentialMoveDict={0:[(-1,0),(1,0),(0,-1),(0,1)],1:[(-1,-1),(1,1),(-1,1),(1,-1)],2:[(-2,-2),(2,2),(-2,2),(2,-2)],3:[(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2)],6:[(-1,0),(1,0)]}

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
    # 0 red   red on top
    # 1 black   black below

    def __init__(self,boardSurface,_type,playerType,initX,initY,size):
        super().__init__()
        self.cellSize=size
       
        self.type=_type
        self.playerType=playerType
        self.X=initX
        self.Y=initY
        self.selected=False
        
        self.empty = pygame.Color(0,0,0,0)
        self.initialize()
       
    def initialize(self): #easier to pickle
        self.image=pygame.Surface((self.cellSize,self.cellSize),pygame.SRCALPHA)
        self.font=pygame.font.SysFont("hiraginosansgbttc",40)
        if (self.playerType==0):
            self.color=(255,0,0)
            self.text = self.font.render (PieceName0[self.type], True, (255, 0, 0))
        else:
            self.color=(0,0,0)
            self.text = self.font.render (PieceName1[self.type], True, (0, 0, 0))
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
            #pygame.draw.circle(self.image,(255,0,0), (self.cellSize// 2, self.cellSize// 2),25,1)
            gfxdraw.aacircle(self.image, self.cellSize// 2, self.cellSize// 2, 20,self.color)
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
    def is_clicked(self,pos):
        return self.rect.collidepoint(pos)
    def potentialMove(self,rowNumber,colomnNumber,PiecesObject):
        moves=[]
        moves2=[]
        if self.type==0 or self.type==1:
            for i in potentialMoveDict[self.type]:
                if self.playerType==0:
                    if self.isInside(rowNumber,colomnNumber,i) and 3<=(self.X+i[0])<=5 and 0<=(self.Y+i[1])<=2:
                        moves.append(i)
                else:
                    if self.isInside(rowNumber,colomnNumber,i) and 3<=(self.X+i[0])<=5 and 7<=(self.Y+i[1])<=9:
                        moves.append(i)

        elif self.type==2:
            for i in potentialMoveDict[self.type]:
                if self.playerType==0:
                    if self.isInside(rowNumber,colomnNumber,i) and PiecesObject[self.Y+((i[1])//2)][self.X+(i[0]//2)]==None and  0<=(self.Y+i[1])<=4:
                        moves.append(i)
                else:
                    if self.isInside(rowNumber,colomnNumber,i) and PiecesObject[self.Y+((i[1])//2)][self.X+(i[0]//2)]==None and  5<=(self.Y+i[1])<=9:
                        moves.append(i)

        elif self.type==3:
            if self.isInside(rowNumber,colomnNumber,(2,-1)) and PiecesObject[self.Y][self.X+1]==None:
                moves.append((2,-1))
            if self.isInside(rowNumber,colomnNumber,(2,1)) and PiecesObject[self.Y][self.X+1]==None:
                moves.append((2,1)) #right 
            if self.isInside(rowNumber,colomnNumber,(1,-2)) and PiecesObject[self.Y-1][self.X]==None:
                moves.append((1,-2))
            if self.isInside(rowNumber,colomnNumber,(-1,-2)) and PiecesObject[self.Y-1][self.X]==None:
                moves.append((-1,-2)) #top
            if self.isInside(rowNumber,colomnNumber,(-2,1)) and PiecesObject[self.Y][self.X-1]==None:
                moves.append((-2,1))
            if self.isInside(rowNumber,colomnNumber,(-2,-1)) and PiecesObject[self.Y][self.X-1]==None:
                moves.append((-2,-1)) #left
            if  self.isInside(rowNumber,colomnNumber,(1,2)) and PiecesObject[self.Y+1][self.X]==None:
                moves.append((1,2))
            if  self.isInside(rowNumber,colomnNumber,(-1,2)) and PiecesObject[self.Y+1][self.X]==None:
                moves.append((-1,2)) #bottom
        elif self.type==4:
            for i in range(self.X-1,-1,-1):# to the left
                if PiecesObject[self.Y][i]==None:
                    moves.append((i-self.X,0))
                else:
                    moves.append((i-self.X,0))
                    break     # add the first non empty place
            for i in range(self.X+1,colomnNumber+1,1):# to the right
                if PiecesObject[self.Y][i]==None:
                    moves.append((i-self.X,0))
                else:
                    moves.append((i-self.X,0))
                    break     # add the first non empty place
            for i in range(self.Y+1,rowNumber+1,1):# to the bottom
                if PiecesObject[i][self.X]==None:
                    moves.append((0,i-self.Y))
                else:
                    moves.append((0,i-self.Y))
                    break     # add the first non empty place
            for i in range(self.Y-1,-1,-1):# to the top
                if PiecesObject[i][self.X]==None:
                    moves.append((0,i-self.Y))
                else:
                    moves.append((0,i-self.Y))
                    break     # add the first non empty place
        # to do cannon
        elif self.type==5:
            for i in range(self.X-1,-1,-1):# to the left
                if PiecesObject[self.Y][i]==None:
                    moves.append((i-self.X,0))
                else:
                    for j in range(i-1,-1,-1):
                        if PiecesObject[self.Y][j]!=None:
                            moves.append((j-self.X,0))
                            break
                    break
            for i in range(self.X+1,colomnNumber+1,1):# to the right
                if PiecesObject[self.Y][i]==None:
                    moves.append((i-self.X,0))
                else:
                    for j in range(i+1,colomnNumber+1,1):
                        if PiecesObject[self.Y][j]!=None:
                            moves.append((j-self.X,0))
                            break
                    break
            for i in range(self.Y+1,rowNumber+1,1):# to the bottom
                if PiecesObject[i][self.X]==None:
                    moves.append((0,i-self.Y))
                else:
                    for j in range(i+1,colomnNumber+1,1):
                        if PiecesObject[j][self.X]!=None:
                            moves.append((0,j-self.Y))
                            break
                    break
            for i in range(self.Y-1,-1,-1):# to the top
                if PiecesObject[i][self.X]==None:
                     moves.append((0,i-self.Y))
                else:
                    for j in range(i-1,-1,-1):
                        if PiecesObject[j][self.X]!=None:
                            moves.append((0,j-self.Y))
                            break
                    break
                        
            
            




        elif self.type==6:        
            if self.playerType==0:    # red top player
                if self.Y<5:
                    moves.append((0,1))   #only go forward
                else:
                    for i in potentialMoveDict[self.type]:
                        if self.isInside(rowNumber,colomnNumber,i):
                            moves.append(i)
                    if self.isInside(rowNumber,colomnNumber,(0,1)):
                            moves.append((0,1)) # go forward if it is still inside 
            else:
                if self.Y>=5:
                    moves.append((0,-1))   #only go forward
                else:
                    for i in potentialMoveDict[self.type]:
                        if self.isInside(rowNumber,colomnNumber,i):
                            moves.append(i)
                    if self.isInside(rowNumber,colomnNumber,(0,-1)):
                            moves.append((0,-1)) # go forward if it is still inside 
        # filter one more time, the the potential move cannot land on your own 
        print(moves)
        for i in moves:
            if  PiecesObject[self.Y+i[1]][self.X+i[0]]==None or PiecesObject[self.Y+i[1]][self.X+i[0]].playerType!=self.playerType:
                moves2.append((self.X+i[0],self.Y+i[1]))
        #print(moves2)
        return moves2

    def isInside(self,rowNumber,colomnNumber,i):
        return (i[0]+self.X)>=0 and (i[0]+self.X)<=colomnNumber and (i[1]+self.Y)>=0 and (i[1]+self.Y)<=rowNumber

        
                
   