# Sonali Singh and Anjali Mangla
# World's Hardest Game MAIN CODE!
# Sources: 
# https://www.pygame.org/docs/tut/tom_games4.html
# https://www.cs.ucsb.edu/~pconrad/cs5nm/topics/pygame/drawing/
# https://pythonprogramming.net/displaying-images-pygame/
# https://pythonprogramming.net/pygame-button-function-events/
# https://freearchives.org
# OMH: Sonali Singh
# OMH: Anjali Mangla

# Explanation: The problem you're solving is the World's Hardest Game. The goal is to make it back to the starting green space after collecting all the coins. If you crash into a blue ball or a black space, you die. We count your deaths - the lower that number is, the better! Purple blocks are walls and white blocks are moving safe spaces. Good luck! Try not to die! Instructions are on the start screen and you can press p to play again or q to quit at any time.

# CODE STARTS HERE!!!
# importing all relevant libraries and classes
import pygame, sys

# class that creates walls (see class for info on attributes)
from barriers import Barriers

# class that creates balls and moving blocks (see class for info on attributes)
from init_balls import CreateBall
import csv

# class that creates player (see class for info on moving methods)
from player2 import Player
import math

# initializing pygame
pygame.display.init()
pygame.init()
Clock = pygame.time.Clock()

# creating game surface
surface = pygame.display.set_mode((677,446))

# creating walls
wall = Barriers(surface)

# drawing black and green walls 
wall.display(1)

# function used for easiness in text display
def text_display(message, size, posx, posy, color):
	text_font = pygame.font.SysFont("freesansbold.ttf", size)

	# creates text
	text = text_font.render(message, True, color)
	text_rect = text.get_rect()

	# location for text
	text_rect.center = (posx, posy)

	# puts text on surface at given location
	surface.blit(text, text_rect)

# loads moving balls and coins
def load_balls():
	balls = []

	# reading in ball data from csv file for flexibility
	with open('balls.csv') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')

		# creating ball objects using CreateBall class
		for row in csv_reader:
			balls.append(CreateBall(surface, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))

	return balls

# loading the balls into a list
balls = load_balls()

# re-draws background function to be used everytime player dies
def loadBackground():
	surface = pygame.display.set_mode((677,446))

	# draws background onto surface
	surface.blit(background, rect)

	# displays green and black walls
	wall.display(1)

	#creates player in starting position
	player.posx = 75
	player.posy = 373
	# moves player 1 unit to display on top of re-drawn green space
	player.moveRight(1)
	

	# makes ball oscillate (direction specified in class) and erases trail by blitting background on previous ball location
	for ball in balls:
		surface.blit(background, ball.image, ball.image)
		ball.oscillate_direction()
		
# HERE WE INITIALIZE MOST OF THE VARIABLES NEEDED IN THE CODE
# counts how many times player has died
death = 0

# counts how many coins player has collected
coins = 0

# total_coins is total number of coins in balls list (36)
total_coins = 0
for ball in balls:
	if ball.kind == 3:
		total_coins += 1

# keeps track of what coins player has collected
coins_gotten = []

# safe determines if the player is on the moving block. If they are, then they are safe and safe = True. If not, the black spaces can kill them, so safe = False.
safe = False

# while loop will run until we tell it that done = True.
done = False


# load and play music!
pygame.mixer.music.load('worldshardestaudio.mp3')
pygame.mixer.music.play(-1)

# finally set up our background by loading our background picture and fitting it to our surface size, then blitting it onto the surface.
background = pygame.image.load('background.png')
background = pygame.transform.scale(background,(677,446))
rect = background.get_rect()
rect = rect.move((0,0))
surface.blit(background,rect)

# this is where the fun starts! lots and lots of collision detection needs to be done for the player.
def collision_detection():
	# these are all the variables that will be changing based on collisions
	global death
	global coins
	global safe
	global player
	global noMoveLeft
	global noMoveRight
	global noMoveUp
	global noMoveDown

	# these variables control movement into the purple walls (kind = 1). When the player comes into contact with a wall, depending where the wall is, they will not be able to move in that direction, and some of these variables will be made true.
	noMoveRight = False
	noMoveLeft = False
	noMoveUp = False
	noMoveDown = False

	# checking collisions with moving blue balls (kinds 1 and 2)
	for ball in balls:
		# distance formula to check for collision
		if math.sqrt(((player.posx+7.5)- ball.posx)**2 + ((player.posy+7.5) - ball.posy)**2) < 12:

			# if player collides with blue ball... they die and their coins are reset
			if ball.kind == 1 or ball.kind == 2:				
				death += 1
				coins = 0

				# empty out coins (balls kind 3) from coins_gotten list and put them back into balls list to redisplay
				# note you'll see two for loops being used for these lines throughout the code because if we put them in the same for loop, the game glitched.
				for ball in coins_gotten:
					balls.append(ball)
				for ball in coins_gotten:
					coins_gotten.remove(ball)

				# reloads and initializes game
				loadBackground()

			# collision with a coin!
			elif ball.kind == 3:
				# increment coin count
				coins += 1
				# remove the coin we collected from the balls list so it doesn't display!
				balls.remove(ball)
				coins_gotten.append(ball)
				surface.blit(background, ball.image, ball.image)

	# checking collisions with black spaces and purple walls
	for barrier in wall.barriers:
		# checks to see if player is in barrier area
		if (barrier.getPosx() -7 )<= player.posx +7.5 <=(barrier.getPosx() + barrier.getDimw() +7) and (barrier.getPosy() -7) <= player.posy +7.5 <= (barrier.getPosy() + barrier.getDimh() + 7):

			# if they are, if the barrier area is black and the player is not on a safely moving block... they die. 
			if barrier.getKind() == 2 and safe == False:
				# death is incremented and coins are reset.
				death += 1
				coins = 0
				# same idea of re-displaying coins.
				for ball in coins_gotten:
					balls.append(ball)
				for ball in coins_gotten:
					coins_gotten.remove(ball)

				# reloads and initializes game
				loadBackground()

			# since the green space is the start and end space, every time the player is in this area, the program checks if they've collected all the coins and if they've won.
			if barrier.getKind() == 3:
				checkCoins()

			# if player comes into contact with a purple wall (kind 1), they can't move into it.
			if barrier.getKind() == 1:
				# if statements determine which direction player can't move based on where the wall is in relation to the player.
				if player.posx <= barrier.getPosx():
					noMoveRight = True
				if player.posx >= barrier.getPosx():
					noMoveLeft = True
				if player.posy <= barrier.getPosy():
					noMoveDown = True
				if player.posy >= barrier.getPosy():
					noMoveUp = True

	# looks for collisions with moving blocks (kinds 4 and 5)
	for ball in balls:
		# a bit more leeway in collisions because the blocks are moving!!
		if (ball.posx -16)<= player.posx +7.5 <=(ball.posx + 75 +16) and (ball.posy -16) <= player.posy +7.5 <= (ball.posy + 75 +16):

			# for the moving vertically block
			if ball.kind == 4:
				# the player is safe and cannot die by black space while on the block
				safe = True

				# these statements move the player at the same speed as the block, so the player can remain on the block, and updates the display so the player shows on top of the moving block.
				if ball.speed > 0:
					surface.blit(background, player.image, player.image)
					if player.posy<443:
						player.moveDown(3)
				elif ball.speed < 0:
					surface.blit(background, player.image, player.image)
					player.moveUp(3)
				pygame.display.update()

			# for the moving horizontally block
			elif ball.kind == 5:
				# exact same idea as above
				safe = True
				if ball.speed < 0:
					surface.blit(background, player.image, player.image)
					player.moveLeft(3)
				elif ball.speed > 0:
					surface.blit(background, player.image, player.image)
					player.moveRight(3)
				pygame.display.update()

			# once the player exits the safe white block, death is fair game... if they move into a black space or crash into a blue ball, they can die.
			else:
				safe = False

# creates start screen
def game_intro():
	# every time game is restarted, player is reset and number of deaths and coins are reset to 0.
	global player
	global death
	global coins
	death = 0
	coins = 0
	intro = True

	# while the intro is running, make the screen white.
	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		surface.fill((255,255,255))

		# these are the instructions and intro to the game, displayed using our nifty text_display function.
		text_display("World's Hardest Game", 60, (677/2), 100, (0,0,0))
		text_display("Read to survive: Use your arrows to move. Avoid blue balls and black spaces. If you don't... DEATH.", 20, (677/2), 200, (0,0,0))
		text_display("Your goal: Collect coins and make it back to the green space to win.", 20, (677/2), 250, (0,0,0))
		text_display("But be careful: We're counting your deaths...", 20, (677/2), 300, (0,0,0))
		text_display("If you're scared... press q to quit or p to try again!", 20, (677/2), 350, (0,0,0))
		
		# draws START button for user
		pygame.draw.rect(surface, (255,0,0), (288, 375, 100, 50))
		text_display("START!", 20, 337, 400, (0,0,0))

		# keeps updating display
		pygame.display.update()
		Clock.tick(15)

		# if player clicks on button (or anywhere on screen) game will begin!
		click = pygame.mouse.get_pressed()
		if click[0] == 1:
			# background re-loads and player re-sets and they're off to playing again!
			background = pygame.image.load('background.png')
			background = pygame.transform.scale(background,(677,446))
			rect = background.get_rect()
			rect = rect.move((0,0))
			surface.blit(background,rect)
			player = Player(surface, background, 75, 373, (255,0,0),15,15)
			break

game_intro()

# checks to see if player has collected all the coins and can win.
def checkCoins():
	global win
	global balls
	# if the number of coins in the coins_gotten list is equal to the amount of total coins, the player just has to make it back to the green space to win.
	if len(coins_gotten) >= total_coins:
		# once this is true, we remove the coins collected from the list and re-add them to the starting balls list so the player can play again and re-collect all the coins if they decide.
		for item in coins_gotten:
			balls.append(item)
		
		for item in coins_gotten:
			coins_gotten.remove(item)
		# finally, calls the win screen
		win_screen()



def win_screen():
	# as in true world's hardest game fashion, the player is still "playing" even when they've won... so the screen doesn't clear out.
	text_display("YOU WON!", 30, 60, 370, (0, 0, 0))

	# player can play again or quit.
	text_display("Press P to play again and Q to quit.", 20, 300, 10, (0,0,0))


# these functions constantly occur as game is being played
while not done:
	# this command, position, was used to manually determine where all the walls, balls, blocks, and coins needed to be - extremely helpful, but extremely tedious!
	position = pygame.mouse.get_pos()

	# continously checks if player is colliding into anything and takes necessary action.
	collision_detection()

	# displays total number of player deaths at top of screen
	text_display("Deaths: " + str(death), 30, 50, 15, (0, 0, 0))

	# continously has the balls oscillate and erase their trails
	for ball in balls:
		surface.blit(background, ball.image, ball.image)
		ball.oscillate_direction()
		
	# if player wants to quit or play again
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		elif event.type == pygame.KEYDOWN:
			# press q to quit at anytime
			if event.key == pygame.K_q:
				done = True
			# press p to play again, and starting screen is recalled 
			elif event.key == pygame.K_p:
				wall.display(1)
				game_intro()

	# these functions correspond to the arrow keys. If arrow keys are pressed, player moves.
	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT]:
		# if player wants to move left and is not at the edge of the screen or in contact with a wall... it can!
		if player.posx > 5:
			if noMoveLeft == False:
				surface.blit(background, player.image, player.image)
				# calls function in player class with given distance to move as argument
				player.moveLeft(5)

	# same idea as above
	if keys[pygame.K_RIGHT]:
		if player.posx < 671 - player.width:
			if noMoveRight == False:
				surface.blit(background, player.image, player.image)
				player.moveRight(5)

	# same idea as above
	if keys[pygame.K_UP]:
		if player.posy > 34:
			if noMoveUp == False:
				surface.blit(background, player.image, player.image)
				player.moveUp(5)

	# same idea as above
	if keys[pygame.K_DOWN]:
		if player.posy < 442 - player.height:
			if noMoveDown == False:
				surface.blit(background, player.image, player.image)
				player.moveDown(5)
	# continously redraw the purple walls so the player can always see them and know not to collide with them
	wall.display(2)
	msElapsed = Clock.tick(20)

	# and of course this continously reupdates our display to show all of this lovely code!
	pygame.display.flip()

