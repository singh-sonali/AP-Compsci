class Element:
	#init function specifies all of our arguments
	def __init__(self, element, number, symbol, weight):
		self.element = element
		self.number = number
		self.symbol = symbol
		self.weight = weight

	#accessor methods
	def getElement(self):
		return self.element
	def setElement(self,element):
		self.element = element
	def getNumber(self):
		return self.number
	def setNumber(self):
		self.number = number
	def getSymbol(self):
		return self.symbol
	def setSymbol(self):
		self.symbol = symbol
	def getWeight(self):
		return self.weight
	def setWeight(self):
		self.weight = weight


	def __str__(self):
		info = "Element name: " + self.element
		info += "\nAtomic number: " + str(self.number)
		info += "\nSymbol: " + self.symbol
		info += "\nAtomic weight: " + str(self.weight) + " g"
		return info


# element1 = Element("Hydrogen", 1, "H", 1.01)
# print(element1)