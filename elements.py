# Sonali Singh and Anjali Mangla
# November 12, 2018
# Sources:
# http://ozzmaker.com/add-colour-to-text-in-python/
# OMH: I have neither given nor received any unauthorized aid.

# creates element object with all of its data
class Element:

	# init function initializes all element characteristics
	def __init__(self, element, number, symbol, weight):
		self.element = element
		self.number = number
		self.symbol = symbol
		self.weight = weight

	# accessor methods
	# useful for privacy
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

	# prints "pretty"
	def __str__(self):

		# info string contains all of element's data with labels in front
		# used ansi escape codes to change the colors of the printed information
		info = "\033[1;31;48m\nElement name: \033[0;30;48m" + self.element
		info += "\033[1;31;48m \nAtomic number: \033[0;30;48m" + str(self.number)
		info += "\033[1;31;48m \nSymbol: \033[0;30;48m" + self.symbol
		info += "\033[1;31;48m \nAtomic weight: \033[0;30;48m " + str(self.weight) + " g/mol"
		return info
