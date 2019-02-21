import pygame
class Player(pygame.sprite.Sprite):

	def __init__(self, surface, background, posx, posy, color, width, height):
		super().__init__()
		self.surface = surface
		self.background = background
		self.posx = posx
		self.posy = posy
		self.color = color
		self. width = width
		self. height = height
		# self.image = pygame.Surface([width, height])
		# self.image.fill((255, 255, 255))
		# self.image.set_colorkey((255, 255, 255))
		self.image = pygame.draw.rect(self.surface, color, [posx, posy, width, height])
		#self.rect = self.image.get_rect()
		#surface.blit(self.image, self.rect)

	def moveRight(self, delta_x):
		posx = self.posx + delta_x
		self.__init__(self.surface, self.background, posx, self.posy, self.color, self.width, self.height)

	def moveLeft(self, delta_x):
		posx = self.posx - delta_x
		self.__init__(self.surface, self.background, posx, self.posy, self.color, self.width, self.height)

	def moveUp(self, delta_y):
		posy = self.posy - delta_y
		self.__init__(self.surface, self.background, self.posx, posy, self.color, self.width, self.height)

	def moveDown(self, delta_y):
		posy = self.posy + delta_y
		self.__init__(self.surface, self.background, self.posx, posy, self.color, self.width, self.height)


