import pygame,sys
from pygame.locals import * 
from Board import Board
from Piece import Piece
pygame.init ()  
screen = pygame.display.set_mode ((1000, 800))  # a surface. 
screen.fill((255,255,255))
pygame.display.flip()
board=Board(screen,50)
board.initializePieces()
while True:
    board.drawBoard()
    board.drawPieces()


    pygame.display.flip() # draw the content
    for events in pygame.event.get():
        if events.type == QUIT:
            sys.exit(0)