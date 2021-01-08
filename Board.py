import pygame
from Piece import Piece 
from Hint import Hint
initialPosition={0:[(4,0)],1:[(3,0),(5,0)],2:[(2,0),(6,0)],3:[(1,0),(7,0)],4:[(0,0),(8,0)],5:[(1,2),(7,2)],6:[(0,3),(2,3),(4,3),(6,3),(8,3)]}
# x,y  coordinate system all the way

#start with 0,0    because we need to 
class Board:
    def __init__(self,n,playerType,screen,cellSize):
        """
        docstring
        4 row 
        river 
        4 row 

        8 column
        """
        self.Row=9
        self.Column=8
        self.cellSize=cellSize
        #self.surf = pygame.Surface(((self.Column+2)*self.cellSize,(self.Row+2)*self.cellSize))
        self.surf=screen
        self.surf.fill((0,255,0))
        self.width=cellSize*self.Row
        self.height=cellSize*self.Column
        self.Color_line=(0,0,0)
        self.playerType=playerType # o is red starts first, 1 is black. 
        self.currentPlayer=0   #red start first
        #self.pieces=[[-1]*(self.Column+1)]*(self.Row+1)   # wrong 
        self.pieces=[[None for i in range(self.Column+1)] for j in range(self.Row+1)]
        #access the self.pieces [Y][X]
        self.hints=[[Hint(self.surf,i,j,self.cellSize) for i in range(self.Column+1)] for j in range(self.Row+1)]
        #access the hint [Y][X]
        self.screen=screen
        #self.pieces[0][0]=Piece(self.surf,0,0,0,0,self.cellSize)
        self.selectedPiece=None
        self.font=pygame.font.SysFont("hiraginosansgbttc",20)
        self.textTopRed = self.font.render ("You are red", True, (255, 0, 0))
        self.textTopBlack=self.font.render ("You are Black", True, (0, 0, 0))
        self.textBottom1=self.font.render ("Your turn", True, (128, 0, 128))
        self.textBottom2=self.font.render ("Opponent's turn", True, (128, 0, 128))
        self.textTopPos = self.textTopRed.get_rect ()
        self.textTopPos.center=(self.surf.get_rect().centerx,20)
        self.textBottomPos = self.textBottom1.get_rect ()
        self.textBottomPos.center=(self.surf.get_rect().centerx,self.surf.get_rect().height-30)
        self.textBottomPos2 = self.textBottom2.get_rect ()
        self.textBottomPos2.center=(self.surf.get_rect().centerx,self.surf.get_rect().height-30)
        self.From=None
        self.To=None
        self.RECTANGLE=pygame.Rect(0, 0, self.cellSize, self.cellSize)
        self.network=n



        '''
    @staticmethod
    def potentialMove(_type):
        if (_type==0):'''


    def drawBoard(self):
        #self.surf.fill((0,255,0)) # fill up all the so that the pieces can move arround
        pygame.draw.line(self.surf, self.Color_line,(self.cellSize,self.cellSize), ((self.Column+1)*self.cellSize, self.cellSize),3)
        pygame.draw.line(self.surf, self.Color_line,(self.cellSize,self.cellSize), (self.cellSize,(self.Row+1)*self.cellSize),3)
        pygame.draw.line(self.surf, self.Color_line,(self.cellSize,(self.Column+2)*self.cellSize),((self.Column+1)*self.cellSize,(self.Row+1)*self.cellSize),3)
        pygame.draw.line(self.surf, self.Color_line,((self.Column+1)*self.cellSize, self.cellSize),((self.Column+1)*self.cellSize,(self.Row+1)*self.cellSize),3)

        for i in range(2,self.Column+1):
            pygame.draw.line(self.surf, self.Color_line,(i*self.cellSize,self.cellSize), (i*self.cellSize, 5*self.cellSize))
            pygame.draw.line(self.surf, self.Color_line,(i*self.cellSize,6*self.cellSize), (i*self.cellSize, (self.Row+1)*self.cellSize))
        for i in range(2,self.Row+1):
            pygame.draw.line(self.surf, self.Color_line,(self.cellSize,i*self.cellSize), ((self.Column+1)*self.cellSize,i*self.cellSize))
        #draw the two cross
        pygame.draw.line(self.surf, self.Color_line,(4*self.cellSize,self.cellSize), (6*self.cellSize, 3*self.cellSize))
        pygame.draw.line(self.surf, self.Color_line,(6*self.cellSize,self.cellSize), (4*self.cellSize, 3*self.cellSize))
        pygame.draw.line(self.surf, self.Color_line,(4*self.cellSize,8*self.cellSize), (6*self.cellSize, 10*self.cellSize))
        pygame.draw.line(self.surf, self.Color_line,(6*self.cellSize,8*self.cellSize), (4*self.cellSize, 10*self.cellSize))
        #pygame.draw.circle(self.surf,self.Color_line,(self.cellSize,self.cellSize),30)
        #pygame.draw.acircle(self.surf, 0, 0, 20, (3,3,3))
        #self.screen.blit(self.surf, (200,40))
        if self.playerType==0: #red
            self.surf.blit(self.textTopRed,self.textTopPos)
        else:
            self.surf.blit(self.textTopBlack,self.textTopPos)
        if self.currentPlayer==self.playerType:
            self.surf.blit(self.textBottom1,self.textBottomPos)
        else:
            self.surf.blit(self.textBottom2,self.textBottomPos2)
        if self.From!=None:
            self.RECTANGLE.center = ((self.From[0]+1)*self.cellSize,(self.From[1]+1)*self.cellSize)
            pygame.draw.rect(self.surf,(0,0,255),self.RECTANGLE,1)
            self.RECTANGLE.center = ((self.To[0]+1)*self.cellSize,(self.To[1]+1)*self.cellSize)
            pygame.draw.rect(self.surf,(0,0,255),self.RECTANGLE,1)
            #pygame.draw.rect(self.surf,(0,0,255),((self.To[0]+1)*self.cellSize,(self.To[1]+1)*self.cellSize,self.cellSize,self.cellSize))
            
    def initializePieces(self):
        #initialize both the object stored in Mattrix 
        for i in initialPosition:
            for j in initialPosition[i]:
                self.pieces[j[1]][j[0]]=Piece(self.surf,i,0,j[0],j[1],self.cellSize)
                self.pieces[self.Row-j[1]][j[0]]=Piece(self.surf,i,1,j[0],self.Row-j[1],self.cellSize)
    

    def drawPieces(self):
        for i in self.pieces:
            for j in i:
                if j!=None:
                    j.draw(self.surf)
    def drawHints(self):
        for i in self.hints:
            for j in i:
                j.draw(self.surf)
    def getClicked(self,pos):
        if self.selectedPiece==None:
            for i in self.pieces:
                for j in i:
                    if j!=None and j.is_clicked(pos) and j.playerType==self.playerType and j.playerType==self.currentPlayer:
                        self.selectedPiece=j
                        j.select()
                        lists=j.potentialMove(self.Row,self.Column,self.pieces) # all the legal point
                        self.switchOnHints(lists)

        elif self.movePiece(pos):
            self.network.send(self.sendBoardData())
            self.deselect()
        else:
            self.deselect()
            self.getClicked(pos)
        
    def movePiece(self,pos):
        if self.selectedPiece!=None:
            for i in self.hints:
                for j in i:
                    if j.getShow() and j.is_clicked(pos):
                        from_temp=(self.selectedPiece.X,self.selectedPiece.Y)
                        to_temp=(j.X,j.Y)
                        self.setFromTo(from_temp,to_temp)
                        return True

    def deselectHints(self):
        for i in self.hints:
            for j in i:
                j.switchOff()
    def switchOnHints(self,listOfHints):
        for i in listOfHints:
            self.hints[i[1]][i[0]].switchOn()


    def deselect(self):
        self.selectedPiece.deselect()
        self.selectedPiece=None
        self.deselectHints()

        
    def print(self):
        for i in self.pieces:
            for j in i:

                print(j,end="")
            print(" ")
    def getPieces(self):
        return self.pieces
    def changePlayer(self):
        if self.currentPlayer==0:
            self.currentPlayer=1
        else:
            self.currentPlayer=0
        print("changing player type")
        print("new player type is")
        print(self.currentPlayer)
    def setFromTo(self,From,To):# change the two position automatically
        self.pieces[From[1]][From[0]].update(To[0],To[1])
        self.pieces[To[1]][To[0]]=self.pieces[From[1]][From[0]] # update the object representation
        self.pieces[From[1]][From[0]]=None
        self.print()
        self.From=From
        self.To=To
        self.changePlayer()
        self.deselectHints()
    def sendBoardData(self):
        temp=[self.From,self.To]
        return temp
    def loadBoardData(self,data):
        self.setFromTo(data[0],data[1])
        self.print()



            



if __name__ == "__main__":
    pygame.init ()  
    screen = pygame.display.set_mode ((1000, 800))  # a surface. 
    board=Board(screen,30)
    board.initializePieces()
    board.print()
    
    
        




