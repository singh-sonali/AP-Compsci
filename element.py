# Compose  a  data  type  Element  for  entries  in  the  periodic  table  of  elements.  Include  data  type  values  for  element,  atomic  number,  symbol,  and  atomic  weight  and  accessor  methods  for  each  of  these  values.  Then,  create  a  data  type  PeriodicTable  that  reads  values  from  a  file  to  create  a  list  of  Element  objects  and  responds  to  queries  on  input  so  that  a  user  can  type  a  molecular  equation  like  H2O  and  the  program  responds  by  printing  the  molecular  weight.  What  other  kinds  of  interactions  can  you  create  within  this  class?  The  file  here:  https://introcs.cs.princeton.edu/python/32class/elements.csv    contains  the  data  that  the  program  should  read.  Include  fields  for  element,  atomic  number,  symbol,  and  atomic  weight.  (Ignore  fields  for  boiling  
# point,  melting  point,  density  (kg/m3),  heat  vapour  (kJ/mol),  heat  fusion  (kJ/mol),  thermal  conductivity  (W/m/K),  and  specific  heat  capacity  (J/kg/K)  since  it's  not  known  for  all  elements).  The  file  is  in  CSV  format  (fields  separated  by  commas).  From:  https://introcs.cs.princeton.edu/python/32class/
class Element:
	def __init__(self, element, number, symbol, weight):
		self.element = element
		self.number = number
		self.symbol = symbol
		self.weight = weight

	def __str__(self):
		info = "Element name: " + self.element
		info += "\nAtomic number: " + str(self.number)
		info += "\nSymbol: " + self.symbol
		info += "\nAtomic weight: " + str(self.weight) + " g"
		return info


# element1 = Element("Hydrogen", 1, "H", 1.01)
# print(element1)