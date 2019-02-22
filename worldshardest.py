import pygame, sys
from barriers import Barriers
from init_balls import CreateBall
import csv
from player2 import Player
import math

pygame.display.init()
pygame.init()
Clock = pygame.time.Clock()
#print(pygame.font.get_fonts())
# instruct_screen()
surface = pygame.display.set_mode((677,446))
def loadBackground():
	surface.blit(background, rect)
	wall.display()
	player = Player(surface, background, 75, 373, (255,0,0),15,15)
	print(player.color)
	# surface.blit(background, player.image, player.image)
	# load_balls()
	for ball in balls:
		surface.blit(background, ball.image, ball.image)
		ball.oscillate_direction()
def text_display(message, posx, posy, color):
	text_font = pygame.font.SysFont("comicsansms", 20)
	text = text_font.render(message, True, color)
	text_rect = text.get_rect()
	text_rect.center = (posx, posy)
	surface.blit(text, text_rect)
def button(message, x,y,w,h,inactive_c,active_c, action=None):
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		if x+w > mouse[0] > x and y+h > mouse[1] > y:
			pygame.draw.rect(surface, active_c,(x,y,w,h))
			if click[0] == 1 and action != None:
				action()     
		else:
			pygame.draw.rect(surface, inactive_c,(x,y,w,h))

		btn_font = pygame.font.SysFont("comicsansms",20)
		btn = btn_font.render(message, True, (0, 0, 0))
		btn_rect = btn.get_rect()
		btn_rect.center = (x + (w/2), (y + (h/2)))
		surface.blit(btn, btn_rect)
def instruct_screen():
	surface.fill((255, 255, 255))
	text_display("HOW TO PLAY", 677/2, 446/2, (0, 0, 0))
	button("CONTINUE (IF YOU DARE)", 677/2, 446 * 2/3, 200, 50, (255, 0, 0), (180, 0, 0), start_screen)

def start_screen():
	surface.fill((255, 255, 255))
	text_display("WELCOME TO THE WORLD'S HARDEST GAME! CLICK START TO BEGIN, THOUGH I THINK IT'S FUNNY YOU THINK YOU CAN BEAT ME.", 677/2, 446/2, (0, 0, 0))
	button("START!", 677/2, 446 * 2/3, 200, 50, 200, 50, (0, 255, 0), (0, 180, 0), loadBackground)


# instruct_screen()
# start_screen()
death = 0
coins = 0
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

wall = Barriers(surface)
wall.display()

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
# player.rect.x = 0
# player.rect.y = 0



def collision_detection():
	global death
	global coins
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
				player.posx = 75
				player.posy = 373
				loadBackground()
				#player.posx = 75
				#player.posy = 373
			elif ball.kind == 3:
				coins += 1
				#balls.remove(ball)
	for barrier in wall.barriers:
		if barrier.getKind() == 2:
			if (barrier.getPosx())<= player.posx +7.5 <=(barrier.getPosx() + barrier.getDimw()) and (barrier.getPosy()) <= player.posy +7.5 <= (barrier.getPosy() + barrier.getDimh()):
				death += 1
				coins = 0
				player.posx = 75
				player.posy = 373
				loadBackground()
		if barrier.getKind() == 1:
			if (barrier.getPosx())<= player.posx +7.5 <=(barrier.getPosx() + barrier.getDimw()) and (barrier.getPosy()) <= player.posy +7.5 <= (barrier.getPosy() + barrier.getDimh()):
				if player.posx <= barrier.getPosx():
					noMoveRight = True
				if player.posx >= barrier.getPosx():
					noMoveLeft = True
				if player.posy <= barrier.getPosy():
					noMoveDown = True
				if player.posy >= barrier.getPosy():
					noMoveUp = True
			
	
while not done:
	collision_detection()
	# wall_collision()
	text_display("Deaths: " + str(death), 30, 10, (0, 0, 0))
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
		if player.posx>0:
			if noMoveLeft == False:
				surface.blit(background, player.image, player.image)
				player.moveLeft(5)
			else:
				pass

	if keys[pygame.K_RIGHT]:
		#if player.rect.x < 677 - player.rect.width:
		if player.posx < 677 - player.width:
			if noMoveRight == False:
				surface.blit(background, player.image, player.image)
				player.moveRight(5)
			else:
				pass

	if keys[pygame.K_UP]:
		#if player.rect.y > 0:
		if player.posy > 0:
			if noMoveUp == False:
				surface.blit(background, player.image, player.image)
				player.moveUp(5)
			else:
				pass

	if keys[pygame.K_DOWN]:
		#if player.rect.y < 446 - player.rect.height:
		if player.posy < 446 - player.height:
			if noMoveDown == False:
				surface.blit(background, player.image, player.image)
				player.moveDown(5)
			else:
				pass

	msElapsed = Clock.tick(20)
	pygame.display.flip()