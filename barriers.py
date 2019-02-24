# SOURCES AND OMH IN MAIN CODE 
# import package for pygame, csv, and import the Create class from init_barrier.py in order to access getter and setter functions
import pygame
import csv
from init_barrier import Create

# Barriers class makes and displays the barriers/walls that are colored purple, green, or black on the background
class Barriers():

	# constructs the barrier/wall arrangement by passing in the game surface, and making a barriers list by taking in values from a csv file called barriers.csv which contains the parameters for the barriers
	def __init__(self, surface):
		super().__init__()
		self.surface = surface

		# reads in barrier parameters from csv and creates objects
		self.barriers = []
		with open('barriers.csv') as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			for row in csv_reader:
				self.barriers.append(Create(row[0], row[1], row[2], row[3], row[4]))
			
	
	# use the getters and setters from init_barrier to, based on the kind of wall (1 = purple, 2 = black, 3 = green safe space) display the wall by getting the values of csv file that specifies the dimensions for that specific wall
	def display(self, choice):
		# choice dictates which barriers we want to display. Since barriers with kind == 1 are the walls that the player can't go past, we want to continously redraw them. So we call display(2).
		if choice == 2:
			for location in self.barriers:
				if location.getKind() == 1: #purple walls
					pygame.draw.rect(self.surface, (255, 100, 255), (location.getPosx(), location.getPosy(), location.getDimw(), location.getDimh()))

		# otherwise, we just want to display the black and green spaces once, so they aren't drawn over the balls or player.
		if choice == 1:
			for location in self.barriers:
				if location.getKind() == 2: #black space
					pygame.draw.rect(self.surface, (0,0,0), (location.getPosx(), location.getPosy(), location.getDimw(), location.getDimh()))

				elif location.getKind() == 3: #green safe space
					pygame.draw.rect(self.surface, (171, 254, 171), (location.getPosx(), location.getPosy(), location.getDimw(), location.getDimh()))

