class Card:
	def __init__(self, rank, suit):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		if self.rank == 11:
			self.rank = "Jack"
		elif self.rank == 12:
			self.rank = "Queen"
		elif self.rank == 13:
			self.rank = "King"
		elif self.rank == 1:
			self.rank = "Ace"
		return str(self.rank) + " of " + str(self.suit)

