# Sonali Singh and Anjali Mangla
# November 12, 2018
# Sources: spread out throughout code on top of functions that use them.
# Source to add colors to text: http://ozzmaker.com/add-colour-to-text-in-python/
# Source for element data: https://introcs.cs.princeton.edu/python/32class/
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
    # Source to learn CSV reading in python: https://realpython.com/python-csv/
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

    # This function calculates the molecular weight in g/mol of any molecular formula that the user puts in by splitting the molecular formula into strings by capital letters, so if the symbol has two letters or one it will be separated, and includes numbers in these separate elements of the list. It then checks which character in the formula is a digit in order to make that the multiplier against the weight of the element in each part of the list.

    # Source to split a string at capital letters: https://stackoverflow.com/questions/2277352/split-a-string-at-uppercase-letters

    def weight(self, formula):
      
        # this sets the multiplier default to 1 if there is no digit (i.e. SiO2 would have just Si, not Si1)
        multiplier = 1
        formula_weight = 0
        result = ""
        # At this point, all variables have been initialized, like the total weight of the formula and what will be printed onto the console (result).

        # split the formula input by finding capital letters and splitting at those points
        split_formula = re.findall('[A-Z][^A-Z]*', formula)
        # default print of result
        result = "\nThat is not a valid entry. Check capitalization and spelling"

        # loop through split_formula list
        for i in range(len(split_formula)):
            # loop through the initial list of element data created in __init__
            for elementdata in self.elements:
                # set position of each character in split_formula to be 0 at first
                pos = 0

                # loop through each character in each element of split_formula in order to find the numbers and take them out of each part of the list so that only the element is remaining
                for letter in split_formula[i]:
                    # check to see if it is a digit, if it is, then make the multiplier the number from that position onwards (if it is two digits or three digits) and then break from the for loop
                    if letter.isdigit():
                        multiplier = int(split_formula[i][pos:])
                        # take out the number so that the element symbol can be found
                        split_formula[i] = split_formula[i].replace(split_formula[i][pos:], "")
                        break
                    # increment position per character
                    pos += 1
                result = "\nThat is not a valid element or formula."
                # check to see if each element of split_formula can be matched with a symbol from self.elements
                if elementdata.symbol == split_formula[i]:
                    # add onto formula_weight the weight of that element * the multiplier saved from above
                    formula_weight += float(elementdata.getWeight())*multiplier
                    # set multiplier back to 1
                    multiplier = 1
                    # add onto the result, rounding the weight
                    result = "\033[1;31;48m\nMolecular Weight: \033[0;30;48m" + str(round(formula_weight , 2)) + " g/mol"
                    # return the result when you have gone through all of split_formula
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