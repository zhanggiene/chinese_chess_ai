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
        self.surf = pygame.Surface((self.Column*self.cellSize+5,self.Row*self.cellSize+5))
        self.surf.fill((0,255,0))
        self.width=cellSize*self.Row
        self.height=cellSize*self.Column
        self.Color_line=(0,0,0)

        
        self.screen=screen
    def draw(self):
        pygame.draw.line(self.surf, self.Color_line,(0,0), ((self.Column)*self.cellSize, 0),3)
        pygame.draw.line(self.surf, self.Color_line,(0,0), (0,(self.Row+1)*self.cellSize),3)
        pygame.draw.line(self.surf, self.Color_line,(0,(self.Column+1)*self.cellSize),((self.Column)*self.cellSize,(self.Column+1)*self.cellSize),3)
        pygame.draw.line(self.surf, self.Color_line,((self.Column)*self.cellSize, 0),((self.Column)*self.cellSize,(self.Row+1)*self.cellSize),3)

        for i in range(1,self.Column):
            pygame.draw.line(self.surf, self.Color_line,(i*self.cellSize,0), (i*self.cellSize, 4*self.cellSize))
            pygame.draw.line(self.surf, self.Color_line,(i*self.cellSize,5*self.cellSize), (i*self.cellSize, self.Row*self.cellSize))
        for i in range(1,self.Row):
            pygame.draw.line(self.surf, self.Color_line,(0,i*self.cellSize), (self.Column*self.cellSize,i*self.cellSize))
        #draw the two cross
        pygame.draw.line(self.surf, self.Color_line,(3*self.cellSize,0), (5*self.cellSize, 2*self.cellSize))
        pygame.draw.line(self.surf, self.Color_line,(5*self.cellSize,0), (3*self.cellSize, 2*self.cellSize))
        pygame.draw.line(self.surf, self.Color_line,(3*self.cellSize,7*self.cellSize), (5*self.cellSize, 9*self.cellSize))
        pygame.draw.line(self.surf, self.Color_line,(5*self.cellSize,7*self.cellSize), (3*self.cellSize, 9*self.cellSize))
        self.screen.blit(self.surf, (200,40))

        
    
        




