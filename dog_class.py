class Dog:

	# constructor
	#scale out of 10
	def __init__(self, name, fullness, energy):
		self.fullness = fullness
		self.energy = energy
		self.happiness = 5
		self.name = name #name is a temporary variable that holds a value

	#methods
	def play(self):
		if self.energy > 0 and self.fullness > 0:
			self.happiness +=1 
			self.fullness -=1
			self.energy -=1
			status = self.name + " played and it was fun."
		else:
			status = "Erm, " + self.name +" shouldn't play right now. Maybe try a nap or some food?"
		return status

	def eat():
		if fullness<10:
			self.happiness +=1
			self.fullness +=1
			self.energy +=1
			status = self.name + " ate some kibble and it was yummy."
		else:
			status = "Your dog is a little full right now. " + self.name " shouldn't eat. Maybe"
	def stats(self):
		info = "Name: " + self.name
		info += "\nEnergy: " + str(self.energy)
		info += "\nHappiness: " + str(self.happiness)
		info += "\nFullness: " + str(self.fullness)
		return info

dog1 = Dog("Tetris", 8, 2)
dog2 = Dog("Finn", 5, 7)

while True:
	print(dog1.stats())
	choice = input("What would you like to do with your dog?")
	if choice == "play":
		print(dog1.play())
	else:
		print("You can't do that.")
