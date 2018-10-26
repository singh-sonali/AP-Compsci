class Student:

	#constructor
	#scale to 10
	def __init__(self,name,money,happiness,intelligence,friends):
		self.name = name
		self.money = money
		self.happiness = happiness
		self.intelligence = intelligence
		self.friends = friends

	def shop(self):
		if wealth > 0:
			wealth -=1
			happiness +=1
			friends +=1
		else:
			print(self.name + " has no money! No shopping allowed.")

	def profile(self):
		info = "Name: " + self.name
		info += "\nMoney: " + str(self.money)
		info += "\nHappiness: " + str(self.happiness)
		info += "\nIntelligence: " + str(self.intelligence)
		info += "\nNumber of friends: " + str(self.friends)
		return info

student1 = Student("Sonali", 10, 10, 10, 100)
print(student1.profile())

while True:
	choice = input("Do you want to shop?")
	if choice == "yes":
		print(student1.shop())
	else:
		print("Sorry, you can't do that.")