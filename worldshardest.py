import pygame
from barriers import Barriers
from init_balls import CreateBall
import csv
from player import Player

pygame.display.init()
Clock = pygame.time.Clock()

surface = pygame.display.set_mode((677,446))
done = False

background = pygame.image.load('background.png')
background = pygame.transform.scale(background,(677,446))
rect = background.get_rect()
rect = rect.move((0,0))
surface.blit(background,rect)

def load_balls():
	wall = Barriers(surface)
	wall.display()
	balls = []
	with open('balls.csv') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		for row in csv_reader:
			balls.append(CreateBall(surface, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
			#print(row)
	return balls


balls = load_balls()


all_sprites_list = pygame.sprite.Group()
player = Player(surface, background, (255, 0, 0), 15, 15)
player.rect.x = 0
player.rect.y = 0
all_sprites_list.add(player)



while not done:
	location = pygame.mouse.get_pos()
	for ball in balls:
		#pygame.display.update() # erases ball
		surface.blit(background,ball.image, ball.image) # at ball.image redraw ball.image
		ball.oscillate_vertical()
		#pygame.display.update()
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	
	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT]:
		if player.rect.x > 0:
			player.moveLeft(5)

	if keys[pygame.K_RIGHT]:
		if player.rect.x < 677 - player.rect.width:
			player.moveRight(5)

	if keys[pygame.K_UP]:
		if player.rect.y > 0:
			player.moveUp(5)

	if keys[pygame.K_DOWN]:
		if player.rect.y < 446 - player.rect.height:
			player.moveDown(5)

	all_sprites_list.update()

	msElapsed = Clock.tick(20)
	pygame.display.flip()
