import pygame,sys
from pygame.locals import * 
from Board import Board
from Piece import Piece
RED=0
BLACK=1

pygame.init ()  
screen = pygame.display.set_mode ((500, 600))  # a surface. 
screen.fill((255,255,255))
pygame.display.flip()
board=Board(0,screen,50)
board.initializePieces()
while True:
   
    screen.fill((255,255,255))
    board.drawBoard()
    board.drawPieces()
    board.drawHints()
    pygame.display.update()
    key = pygame.key.get_pressed()
    if key[pygame.K_DOWN]:
        board.update()
        print("hi,pressed")
    pygame.display.flip() # draw the content
    for events in pygame.event.get():
        if events.type == QUIT:
            sys.exit(0)
        if events.type==MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            board.getClicked(pos)
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_ESCAPE:
                board.deselect()

        