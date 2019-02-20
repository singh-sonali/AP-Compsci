import pygame, sys
import math
from init_balls import Create
import csv
class Ball:
	def __init__(self, surface):
		self.surface = surface
		self.balls = []
		with open('testball.csv') as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			for row in csv_reader:
				self.balls.append(Create(row[0], row[1], row[2], row[3], row[4], row[5]))

	def display(self, newposy):
		for piece in self.balls:
			if piece.kind == "1":
				pygame.draw.circle(self.surface, (0,0,255), [int(piece.posx), int(newposy)], 5)
			pygame.display.update()

	def oscillate_vertical(self):
		for piece in self.balls:
			if piece.kind == "1":
				if int(piece.posy) >= int(piece.lowerlim)-5:
					piece.speed = -1 * int(piece.speed)

				if int(piece.posy) <= int(piece.upperlim)+5:
					piece.speed = -1 * int(piece.speed)
				newposy = (int(piece.posy) + int(piece.speed))
				print(newposy)
				self.display(newposy)

		