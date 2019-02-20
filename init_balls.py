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
		self.image = pygame.draw.circle(self.surface, (self.rcolor, self.gcolor, self.bcolor), [self.posx, self.posy], 5)


	# def display(self, posx, posy, rcolor, gcolor, bcolor):
	# 	for piece in self.balls:
	# 		if piece.kind == "1":
	# 			pygame.draw.circle(self.surface, (int(rcolor), int(gcolor), int(bcolor)), [int(piece.posx), int(newposy)], 5)
			

	def oscillate_vertical(self):
		if int(self.posy) >= int(self.lowerlim):
			self.speed = -1 * int(self.speed)
		if int(self.posy) <= int(self.upperlim):
			self.speed = -1 * int(self.speed)
		newposy = (int(self.posy) + int(self.speed))

		self.__init__(self.surface, self.posx, newposy, self.upperlim, self.lowerlim, self.speed, self.kind, self.rcolor, self.gcolor, self.bcolor)

		

