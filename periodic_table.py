# Sonali Singh and Anjali Mangla
# November 12, 2018
# Sources:
# http://ozzmaker.com/add-colour-to-text-in-python/
# OMH: I have neither given nor received any unauthorized aid.

# importing element class from separate file
from elements import Element
import re
import csv

# this class forms a list with all of the elements in the periodic table
# can be called upon to access information for different elements and formulas.
# reads stored data from a csv file.
class PeriodicTable:

	# sets up elements in PT
	# reads in from 'elements' file using Python's CSV module
	# stored as list of element objects in self.elements list
    def __init__(self):
        self.elements = []
        with open('elements.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                self.elements.append(Element(row[0], row[1], row[2], row[3]))
    
    # prints out all of the data for specified element(s) in the list in a readable fashion
    def __str__(self):
        result = ""

        # each data for element(s) in the list (ex; name, atomic number, etc.) is separated into a diff. line for clarity
        for i in self.elements:
            result += str(i) + "\n"
        return result

    # elchoice function returns all of the data for an element
    def elchoice(self, elchoice):

    	# looks through periodic table list for an element name or symbol that matches the user input
        for elementdata in self.elements:
        	
        	# if found, returns the data for that element
            if elementdata.getElement().upper() == elchoice.upper() or elementdata.getSymbol().upper() == elchoice.upper():
                return elementdata

    # comment here
    def weight(self, formula):
        # be able to divide the molecular formula into elements and add their weights by that and multiplying by the number after it
        multiplier = 1
        formula_weight = 0
        result = ""
        split_formula = re.findall('[A-Z][^A-Z]*', formula)
        result = "\nThat is not a recognizable entry."
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
                    result = "\033[1;31;48m\nMolecular Weight: \033[0;30;48m" + str(round(formula_weight , 2)) + " g/mol"
                    if i == len(split_formula)-1:
                        return result
        return result

    # recognizes whether the user input is an element or a molecular formula, and sets the 'identify' variable accordingly
    def recognize(self, actionchoice):

    	# looks through periodic table list for matching element name or symbol
    	# identify value is True for an element and False for a formula
        for item in self.elements:
            if item.getElement().upper() == actionchoice.upper() or item.getSymbol().upper() == actionchoice.upper(): 
                identify = True
                return identify
            else:
                identify = False
        return identify

# main function with action lines is in separate file

