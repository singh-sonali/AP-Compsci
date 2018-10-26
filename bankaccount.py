import random
class Account:
	def __init__(self, balance, pin):
		self.balance = balance
		self.accnum = random.randrange(10000, 100000)
		self.pin = pin

	def deposit(self, amount):
		self.balance += amount
		status = "You have " + str(self.balance) + " dollars in your bank account."
		return status 
	def withdraw(self, amount):
		if amount <= self.balance:
			self.balance -= amount
			status = "You have " + str(self.balance) + " dollars in your bank account."
		else: 
			status = "INSUFFICIENT FUNDS. You cannot withdraw " + str(self.balance) + " dollars."
		return status
	def transfer(self):
		pass

account1 = Account(1000,1027)
while True:
	choice = input("Would you like to deposit or withdraw? ")
	if choice == "deposit":
		amount = int(input("How much would you like to deposit? "))
		print(account1.deposit(amount))
	if choice == "withdraw":
		amount = int(input("How much would you like to withdraw? "))
		print(account1.withdraw(amount))