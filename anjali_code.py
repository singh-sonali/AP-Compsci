import pygame, sys
from barriers import Barriers
from init_balls import CreateBall
import csv
from player2 import Player
import math

gameState = 0
got_coins = False
pygame.display.init()
pygame.init()
Clock = pygame.time.Clock()
surface = pygame.display.set_mode((677,446))
wall = Barriers(surface)
wall.display(True)
def loadBackground():
	surface.blit(background, rect)
	wall.display(True)
	player = Player(surface, background, 75, 373, (255,0,0),15,15)
	for ball in balls:
		surface.blit(background, ball.image, ball.image)
		ball.oscillate_direction()
def text_display(message, size, posx, posy, color):
	text_font = pygame.font.SysFont("comicsansms", size)
	text = text_font.render(message, True, color)
	text_rect = text.get_rect()
	text_rect.center = (posx, posy)
	surface.blit(text, text_rect)
def button(message, size, x,y,w,h,inactive_c,active_c):
	global gameState
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	if x+w > mouse[0] > x and y+h > mouse[1] > y:
		pygame.draw.rect(surface, active_c,(x,y,w,h))
		if click[0] == 1:
			gameState += 1     
	else:
		pygame.draw.rect(surface, inactive_c,(x,y,w,h))

		btn_font = pygame.font.SysFont("comicsansms",size)
		btn = btn_font.render(message, True, (0, 0, 0))
		btn_rect = btn.get_rect()
		btn_rect.center = (x + (w/2), (y + (h/2)))
		surface.blit(btn, btn_rect)
def instruct_screen():
	surface.fill((255, 255, 255))
	text_display("HOW TO PLAY", 20, 677/2, 446/2, (0, 0, 0))
	button("CONTINUE (IF YOU DARE)", 20, 677/2, 446 * 2/3, 200, 50, (255, 0, 0), (180, 0, 0))

def start_screen():
	surface.fill((255, 255, 255))
	text_display("WELCOME TO THE WORLD'S HARDEST GAME! CLICK START TO BEGIN, THOUGH I THINK IT'S FUNNY YOU THINK YOU CAN BEAT ME.", 10, 677/2, 446/2, (0, 0, 0))
	button("START!", 677/2, 446 * 2/3, 200, 50, (0, 255, 0), (0, 180, 0))


instruct_screen()
start_screen()
death = 0
coins = 0
safe = False
total_coins = 0
coins_gotten = []
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


def load_balls():
	balls = []
	with open('balls.csv') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		for row in csv_reader:
			balls.append(CreateBall(surface, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
			#print(row)
	return balls


balls = load_balls()



#player = Player(surface, background, (255, 0, 0), 15, 15)
player = Player(surface, background, 75, 373, (255,0,0),15,15)



def collision_detection():
	global death
	global coins
	global safe
	global player
	global noMoveLeft
	global noMoveRight
	global noMoveUp
	global noMoveDown
	noMoveRight = False
	noMoveLeft = False
	noMoveUp = False
	noMoveDown = False
	for ball in balls:
		# position of bottom right corner of player is (posx + 15, posy + 15)
		# center of player is (posx + 7.5, posy + 7.5)
		if math.sqrt(((player.posx+7.5)- ball.posx)**2 + ((player.posy+7.5) - ball.posy)**2) < 12:
			print(ball.kind)
			if ball.kind == 1 or ball.kind == 2:
				death += 1
				coins = 0
				for ball in coins_gotten:
					balls.append(ball)
					# coins_gotten.remove(ball)
				for ball in coins_gotten:
					coins_gotten.remove(ball)
				player.posx = 75
				player.posy = 373
				loadBackground()
				#player.posx = 75
				#player.posy = 373
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
				for ball in coins_gotten:
					coins_gotten.remove(ball)
					# coins_gotten.remove(ball)
				player.posx = 75
				player.posy = 373
				loadBackground()

			if barrier.getKind() == 3 and safe == True:
				checkCoins()
				if got_coins == True:
					gameState += 1

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
					surface.blit(ball.surface, player.image, player.image)
					player.moveDown(3)
					pygame.display.update()
				if ball.speed < 0:
					surface.blit(ball.surface, player.image, player.image)
					player.moveUp(3)
					pygame.display.update()
			# if ball.kind == 5:
			# 	safe = True
			# 	if ball.speed < 0:
			# 		player.moveLeft(3)
			# 	if ball.speed > 0:
			# 		player.moveRight(3)

			else:
				safe = False
				#player = Player(surface, background, ball.posx, ball.posy, (255,0,0),15,15)

for ball in balls:
	if ball.kind == 3:
		total_coins += 1
def checkCoins():
	if len(coins_gotten) >= total_coins:
		# will convert to textual message
		print("Ok, so now you have all of the coins! You just have to survive to make it to home base in order to win the world's hardest game.")
		got_coins = True

def win_screen():
	surface.fill(255, 255, 255)
	text_display("YOU WON!", 50, 677/2, 446/2, (0, 0, 0))
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				done = True
	location = pygame.mouse.get_pos()
	print(location)
	print("Game State: " + str(gameState))
	if gameState == 0:
		# instruct_screen()
		pass
	elif gameState == 1:
		# start_screen()
		pass
	elif gameState == 2:
		pass
	elif gameState == 3:
		win_screen()
	print(death)
	print(coins)
	print(len(coins_gotten))
	collision_detection()
	# wall_collision()
	text_display("Deaths: " + str(death), 20, 50, 10, (0, 0, 0))
	text_display("Coins: " + str(coins), 20, 150, 10, (0, 0, 0))
	# font = pygame.font.SysFont("comicsansms", 20)
	# death_text = font.render("hey", True, (0, 0, 0))
	# death_rect = death_text.get_rect()
	# death_rect.center = (x + (w/2), (y + (h/2)))
	# surface.blit(death_text, death_rect)
	for ball in balls:
		surface.blit(background, ball.image, ball.image)
		ball.oscillate_direction()
		
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT]:
		if player.posx > 5:
			if noMoveLeft == False:
				surface.blit(background, player.image, player.image)
				player.moveLeft(5)
			else:
				pass

	if keys[pygame.K_RIGHT]:
		#if player.rect.x < 677 - player.rect.width:
		if player.posx < 671 - player.width:
			if noMoveRight == False:
				surface.blit(background, player.image, player.image)
				player.moveRight(5)
			else:
				pass

	if keys[pygame.K_UP]:
		#if player.rect.y > 0:
		if player.posy > 34:
			if noMoveUp == False:
				surface.blit(background, player.image, player.image)
				player.moveUp(5)

			else:
				pass

	if keys[pygame.K_DOWN]:
		#if player.rect.y < 446 - player.rect.height:
		if player.posy < 442 - player.height:
			if noMoveDown == False:
				surface.blit(background, player.image, player.image)
				player.moveDown(5)
			else:
				pass
	wall.display(False)
	msElapsed = Clock.tick(20)
	pygame.display.flip()
pygame.quit()