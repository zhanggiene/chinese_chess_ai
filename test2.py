import pygame,sys
from pygame.locals import * 
from Board import Board
from Piece import Piece
pygame.init ()  
screen = pygame.display.set_mode ((600, 600))  # a surface. 
screen.fill((255,255,255))
pygame.display.flip()
board=Board(screen,50)
#board.initializePieces()
while True:
   
    screen.fill((255,255,255))
    board.drawBoard()
    board.drawPieces()
    pygame.display.update()
    ev=pygame.event.get()
    board.checkCLicking()
    key = pygame.key.get_pressed()
    if key[pygame.K_DOWN]:
        board.update()
        print("hi,pressed")
    pygame.display.flip() # draw the content
    for events in pygame.event.get():
        if events.type == QUIT:
            sys.exit(0)
        