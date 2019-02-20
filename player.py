import pygame
class Player(pygame.sprite.Sprite):

	def __init__(self, surface, background, color, width, height):
		super().__init__()
		self.surface = surface
		self.background = background
		self.image = pygame.Surface([width, height])
		self.image.fill((255, 255, 255))
		self.image.set_colorkey((255, 255, 255))
		pygame.draw.rect(self.image, color, [0, 0, width, height])
		self.rect = self.image.get_rect()
		surface.blit(self.image, self.rect)
		

		

	def moveRight(self, posx):
		self.rect.x += posx
		pygame.display.update()
		self.surface.blit(self.image, self.rect)


	def moveLeft(self, posx):
		self.rect.x -= posx
		self.surface.blit(self.image, self.rect)

	def moveUp(self, posy):
		self.rect.y -= posy
		self.surface.blit(self.image, self.rect)
	def moveDown(self, posy):
		self.rect.y += posy
		self.surface.blit(self.image, self.rect)
