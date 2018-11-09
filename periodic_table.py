# Things to work on:
# The result of HE2 (need to make else statement?)
# The molecular weight if there are two or more digits
# quit the program
# Move periodic table class to its own file
# comment nicely
import csv
from elements import Element
import re

class PeriodicTable:
	# set up elements in PT
	# read in from file using whatever library
	# stored as list of element objects
    def __init__(self):
        self.elements = []
        with open('elements.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                self.elements.append(Element(row[0], row[1], row[2], row[3]))
      
    def __str__(self):
        result = ""
        for i in self.elements:
            result += str(i) + "\n"
        return result

    def elchoice(self, elchoice):
        for elementdata in self.elements:
            if elementdata.getElement().upper() == elchoice.upper() or elementdata.getSymbol().upper() == elchoice.upper():
                return elementdata
        # noelement = "There is no element by that name/symbol."
        # return noelement

    # comment here
    def weight(self, formula):
        # be able to divide the molecular formula into elements and add their weights by that and multiplying by the number after it
        multiplier = 1
        formula_weight = 0
        result = ""
        split_formula = re.findall('[A-Z][^A-Z]*', formula)
        result = "\nThat is not a valid molecular formula."
        for i in range(len(split_formula)):
            for elementdata in self.elements:
                pos = 0
                for letter in split_formula[i]:
                    if letter.isdigit():
                        multiplier = int(split_formula[i][pos:])
                        split_formula[i] = split_formula[i].replace(split_formula[i][pos:], "")
                        break
                    pos += 1
                result = "\nThat is not a valid element or formula."
                if elementdata.symbol == split_formula[i]:
                    formula_weight += float(elementdata.getWeight())*multiplier
                    multiplier = 1
                    result = "Weight: " + str(round(formula_weight , 2)) + " g"
                    if i == len(split_formula)-1:
                        return result
        return result

    def recognize(self, actionchoice):
        #recognizes whether the user input is an element or a molecular formula
        for item in self.elements:
            if item.getElement().upper() == actionchoice.upper() or item.getSymbol().upper() == actionchoice.upper(): 
                identify = True
                return identify
            else:
                identify = False
        return identify

