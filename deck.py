from card import Card
from random import sample
class Deck:
	def __init__(self, cards):
		if cards == 0:
			self.cards = []
		if cards == 1:
			self.cards = []
			for x in range(1,14):
				self.cards.append(Card(x, "Hearts"))
				self.cards.append(Card(x, "Diamonds"))
				self.cards.append(Card(x, "Clubs"))
				self.cards.append(Card(x, "Spades"))
	def deal(self):
		self.cards.remove(dealcard)

	def __str__(self):
		status = ""
		for x in range(52):
			status += str(self.cards[x]) + "\n"
		return status
def main():
	print(Deck(1))
	dealcard = Card(1, "Spades")
	print(Deck.deal())

main()
