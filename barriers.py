import pygame
import csv
from init_barrier import Create
class Barriers(pygame.sprite.Sprite):

# def makeGreenSpace():
# 	gs = Wall(3, 316, 152, 127, surface, 3)
# 	gs.display()

	def __init__(self, surface):
		super().__init__()
		self.surface = surface
		self.barriers = []
		with open('barriers.csv') as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			for row in csv_reader:
				self.barriers.append(Create(row[0], row[1], row[2], row[3], row[4]))
			
	

	def display(self,):
		for location in self.barriers:
			if location.getKind() == 1: #purple walls
				pygame.draw.rect(self.surface, (255, 100, 255), (location.getPosx(), location.getPosy(), location.getDimw(), location.getDimh()))

			elif location.getKind() == 2: #black space
				pygame.draw.rect(self.surface, (0,0,0), (location.getPosx(), location.getPosy(), location.getDimw(), location.getDimh()))

			elif location.getKind() == 3: 
				#green safe space
				pygame.draw.rect(self.surface, (0, 255, 100), (location.getPosx(), location.getPosy(), location.getDimw(), location.getDimh()))
			#self.display.update()
		
	def collision(self):
		pass
