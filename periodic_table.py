import csv
from elements import Element
import re

class PeriodicTable:
    def __init__(self):
        self.elements = []
        with open('elements.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                self.elements.append(Element(row[0], row[1], row[2], row[3]))
                # print(f'\t{row[0]} has an atomic number of {row[1]}. Its periodic symbol is {row[2]}, and its atomic weight is {row[3]} g.')
    def __str__(self):
        result = ""
        for i in self.elements:
            result += str(i) + "\n"
        return result

    def elchoice(self, elchoice):
        for elementdata in self.elements:
            if elementdata.getElement().upper() == elchoice.upper():
                return elementdata
        noelement = "There is no element by that name."
        return noelement

    def weight(self, formula):
        # be able to divide the molecular formula into elements and add their weights by that and multiplying by the number after it
        multiplier = 1
        formula_weight = 0
        split_formula = re.findall('[A-Z][^A-Z]*', formula)
        print(split_formula)
        for i in range(len(split_formula)):
            for elementdata in self.elements:
                for letter in split_formula[i]:
                    if letter.isdigit():
                        multiplier = int(letter)
                        split_formula[i] = split_formula[i].replace(letter, "")
                        #split_formula[i].remove(letter)
                if elementdata.getSymbol() == split_formula[i]:
                    formula_weight += float(elementdata.getWeight())*multiplier
                    multiplier = 1
        # for x in split_formula:
        #     for letter in x:
        #         if letter.isdigit():
        #             formula_weight*=int(letter)
        return formula_weight


def main():
	print("Welcome to the Periodic Table Mastery Chart! This program is designed to help the user with chemistry homework and become well-equipped with the elements.\n")
	while True:
		table1 = PeriodicTable()

		actionchoice = input("Would you like to...\n1. Get an element's data\n2. Get a molecular formula's weight?\n>> ")
		if actionchoice == '1':
			elchoice = input("Enter an element name to get its data: ")
			print(table1.elchoice(elchoice))
		if actionchoice == '2':
			formula = input("Enter a molecular formula to get its weight: ")
			print(table1.weight(formula))
		else:
			quit()

main()