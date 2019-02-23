import pygame
class CreateBall:
	def __init__(self, surface, posx, posy, upperlim, lowerlim, speed, kind, rcolor, gcolor, bcolor):
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
		if self.kind == 4 or self.kind == 5:
			self.image = pygame.draw.rect(self.surface, (self.rcolor, self.gcolor, self.bcolor), [self.posx, self.posy, 75, 75])
		else:
			self.image = pygame.draw.circle(self.surface, (self.rcolor, self.gcolor, self.bcolor), [self.posx, self.posy], 5)


	# def display(self, posx, posy, rcolor, gcolor, bcolor):
	# 	for piece in self.balls:
	# 		if piece.kind == "1":
	# 			pygame.draw.circle(self.surface, (int(rcolor), int(gcolor), int(bcolor)), [int(piece.posx), int(newposy)], 5)
	def oscillate_direction(self):
		if self.kind == 1 or self.kind == 4:
			self.oscillate_vertical()
		elif self.kind == 2 or self.kind == 3 or self.kind == 5:
			self.oscillate_horizontal()	

	def oscillate_vertical(self):
			if self.posy >= self.lowerlim:
				self.speed = -1 * self.speed
			if self.posy <= self.upperlim:
				self.speed = -1 * self.speed
			newposy = self.posy + self.speed

			self.__init__(self.surface, self.posx, newposy, self.upperlim, self.lowerlim, self.speed, self.kind, self.rcolor, self.gcolor, self.bcolor)

	def oscillate_horizontal(self):
			if self.posx <= self.lowerlim:
				self.speed = -1 * self.speed
			if self.posx >= self.upperlim:
				self.speed = -1 * self.speed
			newposx = self.posx + self.speed

			self.__init__(self.surface, newposx, self.posy, self.upperlim, self.lowerlim, self.speed, self.kind, self.rcolor, self.gcolor, self.bcolor)

		

