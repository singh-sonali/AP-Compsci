import pygame
from barriers import Barriers
from balls2 import Ball

pygame.display.init()
surface = pygame.display.set_mode((677,446))
done = False

background = pygame.image.load('background.png')
background = pygame.transform.scale(background,(677,446))
rect = background.get_rect()
rect = rect.move((0,0))
surface.blit(background,rect)

def main():
	wall = Barriers(surface)
	wall.display()
	ball = Ball(surface, 1)
	#ball.display(0)
	ball.oscillate_vertical()

while not done:
	location = pygame.mouse.get_pos()
	#print(location)
	main()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	pygame.display.flip()