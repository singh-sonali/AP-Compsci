class RationalNumber:
	def __init__(self, n, d):
		self.n = n
		self.d = d

	def __add__(self, other):
		n = self.n*other.d + self.d*other.n
		d = self.d*other.d
		return RationalNumber(n, d)

	def __sub__(self, other):
		n = self.n*other.d - self.d * other.n
		d = self.d*other.d
		return RationalNumber(n, d)

	def __mul__(self, other):
		n = self.n * other.n
		d = self.d*other.d
		return RationalNumber(n, d)

	def __truediv__(self, other):
		n = self.n * other.d
		d = self.d * other.n
		return RationalNumber(n, d)

	def simplify():
		pass

	# complete this first!
	def __str__(self):
		return str(self.n) + "/" + str(self.d) # fill in code (replace 1)

	__repr__ = __str__ # __repr__ returns a "formal" value of a string, while __str__ returns the "informal value". Because of this __repr__ of a string value can be called as an argument in eval.


def main():
	a = RationalNumber(1, 2)
	b = RationalNumber(1, 3)
	q = RationalNumber(7, 19)
	r = RationalNumber(3, 7)
	print(a) # 1/2
	print(b) # 1/3
	print(a+b) # 5/6
	print(a-b) # 1/6
	print(a*b) # 1/6
	print(q*r)
	print(a/b) # 3/2

main()