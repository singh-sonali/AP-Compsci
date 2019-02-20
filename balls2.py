import pygame, sys
import math
from init_balls import Create
import csv
class Ball:
	def __init__(self, surface, posy):
		self.surface = surface
		self.balls = []
		self.posy = posy
		with open('balls.csv') as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			for row in csv_reader:
				self.balls.append(Create(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
		for piece in self.balls:
			if piece.kind == "1":
				piece.posy = self.posy
				self.image = pygame.draw.circle(self.surface, (int(piece.rcolor), int(piece.gcolor), int(piece.bcolor)), [int(piece.posx), int(piece.posy)], 5)

	#def display(self, posy):
		for piece in self.balls:
			if piece.kind == "1":
				pygame.draw.circle(self.surface, (0,0,255), [int(piece.posx), int(piece.posy)], 5)
			pygame.display.update()

	def oscillate_vertical(self):
		for piece in self.balls:
			if piece.kind == "1":
				print("working")
				if int(piece.posy) >= int(piece.lowerlim)-5:
					piece.speed = -1 * int(piece.speed)

				if int(piece.posy) <= int(piece.upperlim)+5:
					piece.speed = -1 * int(piece.speed)
				
				self.posy = (int(piece.posy) + int(piece.speed))
				print(piece.posy)
			self.__init__(self.surface, self.posy)

			# if piece.getPosy() >= piece.getUpperlim():
			# 	print("working?")
			# 	piece.setSpeed(-1 * int(piece.getSpeed()))
			# 	print(piece.setSpeed())
			# if piece.getPosy() <= piece.getLowerlim():
			# 	piece.setSpeed(-1 * int(piece.getSpeed())) # making sure it is positive
			# #newposy = piece.getPosy() + piece.getSpeed()
			# if piece.getKind() == 1:
			# 	print("hi i'm working")
			# 	piece.setPosy(int(piece.getPosy()) + int(piece.getSpeed())) 
			
