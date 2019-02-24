# SOURCES AND OMH IN MAIN CODE 
import pygame
# class CreateBall creates the ball object from a csv (which can also hold parameters for the moving blocks, so it is extremely versatile as a game object class). It initializes the surface, x and y coordinates of the center of the ball or top left corner of the moving block, the upper and lower limits of oscillation, the speed, the kind (1 and 2 being balls moving in different directions, 3 being coins, and 4 and 5 being moving blocks) and the color of the ball object.
class CreateBall:

	# constructor for the CreateBall class initializes the attributes of the ball object as well as draws a white rectangle for moving blocks, a blue circle for the oscillating blue balls, and a yellow ball for the coins.
	def __init__(self, surface, posx, posy, upperlim, lowerlim, speed, kind, rcolor, gcolor, bcolor):
		# read in from csv as strings so converting to ints
		self.surface = surface
		self.posx = int(posx)
		self.posy = int(posy)
		self.upperlim = int(upperlim)
		self.lowerlim = int(lowerlim)
		self.speed = int(speed)
		self.kind = int(kind)
		self.rcolor = int(rcolor)
		self.gcolor = int(gcolor)
		self.bcolor = int(bcolor)
		# draws moving blocks as squares
		if self.kind == 4 or self.kind == 5:
			self.image = pygame.draw.rect(self.surface, (self.rcolor, self.gcolor, self.bcolor), [self.posx, self.posy, 75, 75])
		# draws balls and coins as circles
		else:
			self.image = pygame.draw.circle(self.surface, (self.rcolor, self.gcolor, self.bcolor), [self.posx, self.posy], 5)

	# called in main function to determine which way balls should oscillate based on their kind
	def oscillate_direction(self):
		# vertical moving balls and blocks are kinds 1 and 4 respectively
		if self.kind == 1 or self.kind == 4:
			self.oscillate_vertical()

		# horizontally moving balls and blocks (or coins that have a speed of 0 and don't oscillate) are kinds 2 (balls), 3 (coins), 5 (blocks)
		elif self.kind == 2 or self.kind == 3 or self.kind == 5:
			self.oscillate_horizontal()	

	# move up and down
	def oscillate_vertical(self):
			# reverse objects direction when it gets to the upper and lower bound as specified in code
			if self.posy >= self.lowerlim:
				self.speed = -1 * self.speed
			if self.posy <= self.upperlim:
				self.speed = -1 * self.speed

			# increments object's position based on speed
			newposy = self.posy + self.speed

			# redraws object in new location
			self.__init__(self.surface, self.posx, newposy, self.upperlim, self.lowerlim, self.speed, self.kind, self.rcolor, self.gcolor, self.bcolor)

	def oscillate_horizontal(self):
		# reverse objects direction when it gets to the upper (right) and lower (left) bound as specified in code
			if self.posx <= self.lowerlim:
				self.speed = -1 * self.speed
			if self.posx >= self.upperlim:
				self.speed = -1 * self.speed

			# increments object's position based on speed
			newposx = self.posx + self.speed

			# redraws object in new location
			self.__init__(self.surface, newposx, self.posy, self.upperlim, self.lowerlim, self.speed, self.kind, self.rcolor, self.gcolor, self.bcolor)

		

