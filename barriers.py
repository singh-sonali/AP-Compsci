import pygame
import csv
from init_barrier import Create
class Barriers():


	def __init__(self, surface):
		super().__init__()
		self.surface = surface
		self.barriers = []
		with open('barriers.csv') as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			for row in csv_reader:
				self.barriers.append(Create(row[0], row[1], row[2], row[3], row[4]))
			
	

	def display(self, choice):
		if choice == 2:
			for location in self.barriers:
				if location.getKind() == 1: #purple walls
					pygame.draw.rect(self.surface, (255, 100, 255), (location.getPosx(), location.getPosy(), location.getDimw(), location.getDimh()))

		elif choice == 1:
			for location in self.barriers:
				if location.getKind() == 2: #black space
					pygame.draw.rect(self.surface, (0,0,0), (location.getPosx(), location.getPosy(), location.getDimw(), location.getDimh()))

				elif location.getKind() == 3: 
					#green safe space
					pygame.draw.rect(self.surface, (171, 254, 171), (location.getPosx(), location.getPosy(), location.getDimw(), location.getDimh()))
		else: 
			self.surface.fill((255,255,255))
