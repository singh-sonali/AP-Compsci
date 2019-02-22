class Create:
	def __init__(self, posx, posy, dimw, dimh, kind):
		self.posx = int(posx)
		self.posy = int(posy)
		self.dimw = int(dimw)
		self.dimh = int(dimh)
		self.kind = int(kind)

	def getPosx(self):
		return self.posx
	def setPosx(self):
		self.posx = int(posx)
	def getPosy(self):
		return self.posy
	def setPosy(self):
		self.posy = int(posy)
	def getDimw(self):
		return self.dimw
	def setDimw(self):
		self.dimw = int(dimw)
	def getDimh(self):
		return self.dimh
	def setDimh(self):
		self.dimh = int(dimh)
	def getKind(self):
		return self.kind
	def setKind(self):
		self.kind = int(kind)


