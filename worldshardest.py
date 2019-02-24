import pygame, sys
from barriers import Barriers
from init_balls import CreateBall
import csv
from player2 import Player
import math


pygame.display.init()
pygame.init()
Clock = pygame.time.Clock()
surface = pygame.display.set_mode((677,446))
wall = Barriers(surface)
wall.display(1)

def load_balls():
	balls = []
	with open('balls.csv') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		for row in csv_reader:
			balls.append(CreateBall(surface, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))

	return balls


balls = load_balls()

def loadBackground():
	surface.blit(background, rect)
	wall.display(1)
	player = Player(surface, background, 75, 373, (255,0,0),15,15)
	for ball in balls:
		surface.blit(background, ball.image, ball.image)
		ball.oscillate_direction()

def text_display(message, size, posx, posy, color):
	text_font = pygame.font.SysFont("freesansbold.ttf", size)
	text = text_font.render(message, True, color)
	text_rect = text.get_rect()
	text_rect.center = (posx, posy)
	surface.blit(text, text_rect)


death = 0
coins = 0
safe = True
total_coins = 0
coins_gotten = []
all_coins = False

done = False

noMoveLeft = False
noMoveRight = False
noMoveUp = False
noMoveDown = False


background = pygame.image.load('background.png')
background = pygame.transform.scale(background,(677,446))
rect = background.get_rect()
rect = rect.move((0,0))
surface.blit(background,rect)

def collision_detection():
	global death
	global coins
	global safe
	global player
	global noMoveLeft
	global noMoveRight
	global noMoveUp
	global noMoveDown
	global all_coins
	noMoveRight = False
	noMoveLeft = False
	noMoveUp = False
	noMoveDown = False
	for ball in balls:
		if math.sqrt(((player.posx+7.5)- ball.posx)**2 + ((player.posy+7.5) - ball.posy)**2) < 12:
			if ball.kind == 1 or ball.kind == 2:
				pass
				# death += 1
				# coins = 0
				# for ball in coins_gotten:
				# 	balls.append(ball)
				# player.posx = 75
				# player.posy = 373
				# loadBackground()
			elif ball.kind == 3:
				coins += 1
				balls.remove(ball)
				coins_gotten.append(ball)

	for barrier in wall.barriers:
		if (barrier.getPosx() -7 )<= player.posx +7.5 <=(barrier.getPosx() + barrier.getDimw() +7) and (barrier.getPosy() -7) <= player.posy +7.5 <= (barrier.getPosy() + barrier.getDimh() + 7):
			if barrier.getKind() == 2 and safe == False:
				death += 1
				coins = 0
				for ball in coins_gotten:
					balls.append(ball)
				player.posx = 75
				player.posy = 373
				loadBackground()

			if barrier.getKind() == 3:
				checkCoins()
				if all_coins == True:
					win_screen()

			if barrier.getKind() == 1:
				if player.posx <= barrier.getPosx():
					noMoveRight = True
				if player.posx >= barrier.getPosx():
					noMoveLeft = True
				if player.posy <= barrier.getPosy():
					noMoveDown = True
				if player.posy >= barrier.getPosy():
					noMoveUp = True
		
	for ball in balls:
		if (ball.posx -16)<= player.posx +7.5 <=(ball.posx + 75 +16) and (ball.posy -16) <= player.posy +7.5 <= (ball.posy + 75 +16):
			if ball.kind == 4:
				safe = True
				if ball.speed > 0:
					surface.blit(background, player.image, player.image)
					if player.posy<443:
						player.moveDown(3)
				elif ball.speed < 0:
					surface.blit(background, player.image, player.image)
					player.moveUp(3)
				pygame.display.update()
			elif ball.kind == 5:
				safe = True
				if ball.speed < 0:
					player.moveLeft(3)
				elif ball.speed > 0:
					player.moveRight(3)
				pygame.display.update()

			else:
				pass
				# safe = False

def game_intro():
	global player
	global death
	global coins
	death = 0
	coins = 0
	total_coins = 0
	intro = True

	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		surface.fill((255,255,255))

		text_display("World's Hardest Game", 60, (677/2), 100, (0,0,0))
		text_display("Read to survive: Avoid blue balls and black spaces. If you don't... DEATH.", 20, (677/2), 200, (0,0,0))
		text_display("Your goal: Collect coins and make it back to the green space to win.", 20, (677/2), 250, (0,0,0))
		text_display("But be careful: We're counting your deaths...", 20, (677/2), 300, (0,0,0))
		
		pygame.draw.rect(surface, (255,0,0), (288, 350, 100, 50))
		text_display("START!", 20, 337, 375, (0,0,0))

		pygame.display.update()
		Clock.tick(15)

		click = pygame.mouse.get_pressed()
		if click[0] == 1:
			background = pygame.image.load('background.png')
			background = pygame.transform.scale(background,(677,446))
			rect = background.get_rect()
			rect = rect.move((0,0))
			surface.blit(background,rect)
			player = Player(surface, background, 75, 373, (255,0,0),15,15)
			break

game_intro()
total_coins = 0
for ball in balls:
	if ball.kind == 3:
		total_coins += 1
print(total_coins)

def checkCoins():
	global all_coins
	global win
	if len(coins_gotten) >= total_coins:
		all_coins = True
		win = True


def win_screen():
	text_display("YOU WON!", 30, 60, 370, (0, 0, 0))
	text_display("Press P to play again and Q to quit.", 17, 60, 400, (0, 0, 0))


while not done:
	position = pygame.mouse.get_pos()
	collision_detection()
	text_display("Deaths: " + str(death), 20, 50, 10, (0, 0, 0))
	text_display("Coins: " + str(coins), 20, 150, 10, (0, 0, 0))
	for ball in balls:
		surface.blit(background, ball.image, ball.image)
		ball.oscillate_direction()
		
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				done = True
			elif event.key == pygame.K_p:
				game_intro()

	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT]:
		if player.posx > 5:
			if noMoveLeft == False:
				surface.blit(background, player.image, player.image)
				player.moveLeft(5)

	if keys[pygame.K_RIGHT]:
		if player.posx < 671 - player.width:
			if noMoveRight == False:
				surface.blit(background, player.image, player.image)
				player.moveRight(5)

	if keys[pygame.K_UP]:
		if player.posy > 34:
			if noMoveUp == False:
				surface.blit(background, player.image, player.image)
				player.moveUp(5)

	if keys[pygame.K_DOWN]:
		if player.posy < 442 - player.height:
			if noMoveDown == False:
				surface.blit(background, player.image, player.image)
				player.moveDown(5)

	wall.display(2)
	msElapsed = Clock.tick(20)
	pygame.display.flip()