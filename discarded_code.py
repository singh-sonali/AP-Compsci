# def __init__(self, posx, posy, dimw, dimh, surface, kind):
	# 	self.posx = posx
	# 	self.posy = posy
	# 	self.dimw = dimw
	# 	self.dimh = dimh
	# 	self.surface = surface
	# 	self.kind = kind

# if self.kind == 1:
		# 	pygame.draw.rect(self.surface, (255, 100, 255), (self.posx, self.posy, self.dimw, self.dimh))

# elif self.kind == 2:
		# 	pygame.draw.rect(self.surface, (0, 0, 0), (self.posx, self.posy, self.dimw, self.dimh))
#pygame.draw.rect(self.surface, (0, 255, 100), (self.posx, self.posy, self.dimw, self.dimh))

def makeWalls():
	#left border
	wall1 = Wall(0, 29, 3, 446, surface,1)
	wall1.display()
	#top border
	wall2 = Wall(0, 29, 677, 3, surface,1)
	wall2.display()
	#right border
	wall3 = Wall(674, 29, 3, 446, surface,1)
	wall3.display()
	#bottom border
	wall4 = Wall(0, 443, 677, 3, surface,1)
	wall4.display()
	#middle long block
	wall5 = Wall(78, 287, 518, 29, surface,1)
	wall5.display()
	#right vertical block
	wall6 = Wall(570, 287, 27, 81, surface,1)
	wall6.display()
	#middle vertical block
	wall7 = Wall(259, 158, 29, 129, surface,1)
	wall7.display()
	#bottom vertical block
	wall8 = Wall(156,391,28,52, surface,1)
	wall8.display()
	#center top vertical block
	wall9 = Wall(259,29,29,79,surface,1)
	wall9.display()
	#center top horizontal block
	wall10 = Wall(259, 80, 185, 29, surface,1)
	wall10.display()
	#right most horizontal block
	wall11 = Wall(389, 158, 130, 27, surface,1)
	wall11.display()
	#right most vertical block
	wall12 = Wall(491,29,28,155, surface,1)
	wall12.display()

def makeBlackSpaces():
	#top left
	bs1 = Wall(3, 32, 101, 23, surface, 2)
	bs1.display()
	#to the right of top left
	bs2 = Wall(156, 32, 101, 23, surface, 2)
	bs2.display()
	#leftmost square
	bs3 = Wall(53, 184, 25, 25, surface, 2)
	bs3.display()
	#square to the right
	bs4 = Wall(105, 107, 25, 25, surface, 2)
	bs4.display()
	#big square
	bs5 = Wall(131, 160, 127, 127, surface, 2)
	bs5.display()
	#bottommost rectangle
	bs6 = Wall(184, 393, 153, 51, surface, 2)
	bs6.display()
	#rectangle up and to the right
	bs7 = Wall(416, 316, 153, 51, surface, 2)
	bs7.display()
	#large long rectangle in middle
	bs8 = Wall(389, 186, 130, 101, surface, 2)
	bs8.display()
	#small square on right of screen
	bs9 = Wall(597, 287, 77, 78, surface, 2)
	bs9.display()
	#large vertical rectangle on right
	bs10 = Wall(519, 32, 155, 255, surface, 2)
	bs10.display()

def makeGreenSpace():
	gs = Wall(3, 316, 152, 127, surface, 3)
	gs.display()