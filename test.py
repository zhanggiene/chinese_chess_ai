import pygame  
from pygame.locals import *  
  
def main ():  
    # Initialise screen  
    pygame.init ()  
    screen = pygame.display.set_mode ((650, 150))   
  
    # Fill background  
    background = pygame.Surface (screen.get_size ())  
    background = background.convert ()  
    background.fill ((250, 250, 250))  
  
    # Display some text  
    #font = pygame.font.Font (None, 60) #Original code, use the default font, can not display Chinese  
    #font = pygame.font.Font ('../FredGuo/simkai.ttf', 60) #Correct, the file name can include the path  
    #font = pygame.font.Font ('italic', 60) #Error, the name parameter should be the font file name  
    font=pygame.font.SysFont("hiraginosansgbttc",50)
    a=pygame.font.get_fonts()
    for b in a:
        print(b)
    #font = pygame.font.SysFont ('nadeemttc', 60) #Correct, the name parameter should be the font name, and the character set should be the same as the system  
    text = font.render ("漢", 1, (10, 10, 10)) #The display content must be converted to Unicode, otherwise Chinese cannot be displayed normally  
    textpos = text.get_rect ()  
    textpos.center = background.get_rect (). center  
    background.blit (text, textpos)  
    cellSize = 20
    size=20
    board = pygame.Surface((cellSize * 8, cellSize * 8))
    board.fill((255, 255, 255))

  
    # Blit everything to the screen  
    screen.blit (background, (0, 0))  
    
  
    # Event loop  
    while 1:  
        for event in pygame.event.get ():  
            if event.type == QUIT:  
                return  
  
        screen.blit (background, (0, 0))  
        screen.blit(board, board.get_rect())
        pygame.draw.line(screen,(255,0,0),(60,80),(100,80))

        pygame.display.flip ()  
  
  
if __name__ == '__main__': main ()