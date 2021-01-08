import pygame,sys
from pygame.locals import * 
from Board import Board
from Piece import Piece
from client import Network
import threading


def main(screen,ID):
    screen.fill((155,255,255))
    pygame.display.flip()
    board=Board(n,ID,screen,50)
    board.initializePieces()
    #n.send(board.sendBoardData())   # initialize the server 
    pygame.display.flip()
    thread2=threading.Thread(target=update,args=(n,board))
    thread2.start()
    
    while True:
        screen.fill((255,255,255))
        board.drawBoard()
        board.drawPieces()
        board.drawHints()
        pygame.display.update()
        for events in pygame.event.get():
            if events.type == QUIT:
                print("quit")
                sys.exit(0)
            if events.type==MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                board.getClicked(pos)
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_ESCAPE:
                    board.deselect()
                if events.key == pygame.K_p:
                    board.setFromTo((0,0),(0,1))
                if events.key == pygame.K_o:
                    board.setFromTo((0,1),(0,0))

RED=0
BLACK=1
playerType=-1

pygame.init ()  
screen = pygame.display.set_mode ((500, 600))  # a surface. 
pygame.display.set_caption("Chinese Chess Game")
run=True
ready=False
clicked=False
font=pygame.font.SysFont("hiraginosansgbttc",30)
textWait=font.render ("wait for other to join", True, (255, 0, 0))
textclick=font.render ("click to join", True, (255, 0, 0))

textPos = textWait.get_rect ()
textPos.center=(screen.get_rect().centerx,100)

def wait(client):
    global playerType,ready
    playerType=int(client.receiveID().decode())
    print("playerTYpe ID is ",playerType)
    ready=True
def update(client,boardChess):
    while True:
        print("receiving the data from server")
        data=client.receive()
        print(data)
        boardChess.loadBoardData(data)


i=1
while run:
    
    screen.fill((i%255,255,255))
    
    
   
    if ready:

        main(screen,playerType)
        run=False
        break
    if clicked:
        i+=5
        screen.blit(textWait,textPos)


    else:
        screen.blit(textclick,textPos)

    for event in pygame.event.get(): # must have conponent
        if event.type == pygame.QUIT:
            run = False
        if event.type==MOUSEBUTTONDOWN and not clicked:
            n=Network()
            thread=threading.Thread(target=wait,args=(n,))
            thread.start()
            clicked=True
    pygame.display.flip()

        







