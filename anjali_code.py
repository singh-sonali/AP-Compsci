
# https://www.pygame.org/docs/tut/tom_games4.html
import pygame, sys
import math
# def oscillate_vertical(posx, posy):
# 	for i in range(height - posy):
# 		ball = Ball(posx, posy)
# 		posy += 1

class Ball:
	def __init__(self, posx, posy, color, speed):
		self.posx = posx
		self.posy = posy
		self.color = color
		self.image = pygame.draw.circle(screen, color, [posx, posy], 5)
		self.speed = speed
	def oscillate_vertical(self):
		# height_screen - 5 is height of screen - radius
		if self.posy >= height_screen - 5:
			self.speed = -1 * self.speed
		if self.posy <= 5:
			self.speed = -1* self.speed # making sure it is positive
		newposy = self.posy + self.speed
		self.__init__(self.posx, newposy, self.color, self.speed)




# class Ball(pygame.sprite.Sprite):
#     """A ball that will move across the screen
#     Returns: ball object
#     Functions: update, calcnewpos
#     Attributes: area, vector"""

#     def __init__(self, posx, posy):
#         super().__init__()
#         self.image = pygame.draw.circle(screen, (0, 0, 255), [posx, posy], 5)
#         self.image.set_colorkey((255, 255, 255))
#         self.posx = posx
#         self.posy = posy

#     def oscillate_vertically(self, posy):
#     	self.posy += 1
# Source: https://www.101computing.net/pygame-how-to-control-your-sprite/
class Player(pygame.sprite.Sprite):

	def __init__(self, color, width, height):
		super().__init__()
		self.image = pygame.Surface([width, height])
		self.image.fill((255, 255, 255))
		self.image.set_colorkey((255, 255, 255))

		pygame.draw.rect(self.image, color, [0, 0, width, height])

		self.rect = self.image.get_rect()

	def moveRight(self, posx):
		self.rect.x += posx

	def moveLeft(self, posx):
		self.rect.x -= posx

	def moveUp(self, posy):
		self.rect.y -= posy

	def moveDown(self, posy):
		self.rect.y += posy

pygame.init()
height_screen = 500
width_screen = 500
size = [width_screen, height_screen]
balls = []
coins = []
screen = pygame.display.set_mode(size)
pygame.display.set_caption("World's Hardest Game! Can you beat it in time?")
done = False
Time = 0
Minute = 0
Hour = 0
Day = 0
time = pygame.time.get_ticks
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

all_sprites_list = pygame.sprite.Group()

player = Player((255, 0, 0), 15, 15)
player.rect.x = 0
player.rect.y = 0

all_sprites_list.add(player)
Font = pygame.font.SysFont("Trebuchet MS", 25)
#Day
DayFont = Font.render("Day:{0:03}".format(Day),1, WHITE) #zero-pad day to 3 digits
DayFontR = DayFont.get_rect()
DayFontR.center=(100,20)
#Hour
HourFont = Font.render("Hour:{0:02}".format(Hour),1, WHITE) #zero-pad hours to 2 digits
HourFontR=HourFont.get_rect()
HourFontR.center=(width_screen - 20,20)
#Minute
MinuteFont = Font.render("Minute:{0:02}".format(Minute),1, WHITE) #zero-pad minutes to 2 digits
MinuteFontR=MinuteFont.get_rect()
MinuteFontR.center=(width_screen - 5,20)

Clock = pygame.time.Clock()
CLOCKTICK = pygame.USEREVENT + 1
pygame.time.set_timer(CLOCKTICK, 1000)
# https://stackoverflow.com/questions/38045189/how-do-i-make-pygame-display-the-time-and-change-it-when-the-time-changes-using
while not done:
	# clock.tick(10)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				done = True
		if event.type == CLOCKTICK:
			Minute = Minute + 1
			if Minute == 60:
				Hour = Hour + 1
				Minute = 0
			if Hour == 12:
				Day = Day + 1
				Hour = 0
			#screen.fill((0, 0, 0))
			# redraw time
			MinuteFont = Font.render("Minute:{0:02}".format(Minute), 1, RED)
			screen.blit(MinuteFont, MinuteFontR)
			HourFont = Font.render("Hour:{0:02}".format(Hour), 1, RED)
			screen.blit(HourFont, HourFontR)
			DayFont = Font.render("Day:{0:03}".format(Day), 1, RED)
			screen.blit(DayFont, DayFontR)

	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT]:
		if player.rect.x > 0:
			player.moveLeft(5)
		else:
			pass
	if keys[pygame.K_RIGHT]:
		if player.rect.x < 500 - player.rect.width:
			player.moveRight(5)
		else:
			pass
	if keys[pygame.K_UP]:
		if player.rect.y > 0:
			player.moveUp(5)
		else:
			pass

	if keys[pygame.K_DOWN]:
		if player.rect.y < 500 - player.rect.height:
			player.moveDown(5)
		else:
			pass

	all_sprites_list.update()

	screen.fill((0, 0, 0))

	posx = int(width_screen/10)
	posy = int(height_screen/5)

	for i in range(5):
		ball = Ball(posx, posy, (0, 0, 255), 5)
		balls.append(ball)
		posx += 100
		# may need to uncomment the comment below

	for i in range(5):
		balls[i].oscillate_vertical()
		pygame.display.update()

	# for i in range(5):
	# 	ball = Ball(balls[i], posy)
	# 	pygame.display.update()
	# 	for i in range(100):
	# 		ball.oscillate_vertical(posy)
	# 	pygame.display.update()
	posx = 100
	posy = 300
	for i in range(3):
		coin = Ball(posx, posy, (255, 255, 0), 0)
		coins.append(coin)
		posx += 150
		pygame.display.update()

	all_sprites_list.draw(screen)


	pygame.display.flip()

	Clock.tick(60)
pygame.quit()
# hints with text box for each level 



