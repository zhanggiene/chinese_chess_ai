import pygame
class Board:
    def __init__(self,screen,cellSize):
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
        self.surf = pygame.Surface(((self.Column+2)*self.cellSize,(self.Row+2)*self.cellSize))
        self.surf.fill((0,255,0))
        self.width=cellSize*self.Row
        self.height=cellSize*self.Column
        self.Color_line=(0,0,0)

        
        self.screen=screen
    @staticmethod
    def potentialMove(_type):
        if (_type==0):
            

    def draw(self):
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
        pygame.draw.circle(self.surf,self.Color_line,(self.cellSize,self.cellSize),30)
        #pygame.draw.acircle(self.surf, 0, 0, 20, (3,3,3))
        self.screen.blit(self.surf, (200,40))

        
    
        




