# SOURCES AND OMH IN MAIN CODE 
import pygame, sys
# use sprite module from the pygame package in order to allow the player to access sprite attributes
class Player(pygame.sprite.Sprite):
	#constructor that takes into account the surface, background, x and y positions, color, and width and height of the player object.
	def __init__(self, surface, background, posx, posy, color, width, height):
		super().__init__()
		self.surface = surface
		self.background = background
		self.posx = posx
		self.posy = posy
		self.color = color
		self. width = width
		self. height = height
		# self.image represents what you seen on the screen, a.k.a. the red square that is the player
		self.image = pygame.draw.rect(self.surface, color, [posx, posy, width, height])

	# move functions for the player based on key presses --> up corresponds to up arrow, down to down, etc.
	def moveRight(self, delta_x):
		# delta_x is almost like the speed of the player; it is what the position increments by every time you move it right or left.
		posx = self.posx + delta_x
		# redraw/initialize the player.
		self.__init__(self.surface, self.background, posx, self.posy, self.color, self.width, self.height)

	def moveLeft(self, delta_x):
		# same as above
		posx = self.posx - delta_x
		# redraw
		self.__init__(self.surface, self.background, posx, self.posy, self.color, self.width, self.height)

	def moveUp(self, delta_y):
		# delta_y is almost like the speed of the player; it is what the position increments by every time you move it up or down.
		posy = self.posy - delta_y
		# redraw
		self.__init__(self.surface, self.background, self.posx, posy, self.color, self.width, self.height)

	def moveDown(self, delta_y):
		# same as above
		posy = self.posy + delta_y
		# redraw
		self.__init__(self.surface, self.background, self.posx, posy, self.color, self.width, self.height)


