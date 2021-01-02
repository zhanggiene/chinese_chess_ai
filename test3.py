import pygame
from pygame.locals import *
 
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((400,300), 0, 32)
pygame.display.set_caption("Game")
x, y = 200, 130
sprite = pygame.image.load("chessbackGround.png")
 
loop = True
pygame.mouse.set_visible(False)
while loop:
	#screen.fill((0,0,0))
	x, y = pygame.mouse.get_pos()
	screen.blit(sprite, (x-50,y-50))
	for event in pygame.event.get():
		if event.type == QUIT:
			loop = False
	pygame.display.flip()
	clock.tick(60)
 
 
pygame.quit()