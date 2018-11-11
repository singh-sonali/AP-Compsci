# Sonali Singh and Anjali Mangla
# November 12, 2018
# Sources:
# http://ozzmaker.com/add-colour-to-text-in-python/
# OMH: I have neither given nor received any unauthorized aid.

# importing periodic_table and element classes from separate files
from elements import Element
from periodic_table import PeriodicTable
import csv
import re

# acts upon user input
def main():

	# creates periodic table object
    table1 = PeriodicTable()
    print("Welcome to the Periodic Table Mastery Chart! This program is designed to help the user with chemistry homework and become well-equipped with the elements.\n")

    while True:
        actionchoice = input("\nEnter an element name, symbol, or molecular formula to access information. (enter Q to quit)\n>> ")

        # user has option to quit
        if actionchoice.upper() == 'Q':
        	print("Bye!")
        	quit()

        # identify value is set in recognize function in PeriodicTable class
        identify = table1.recognize(actionchoice)

        # if user input is recognized as element, elchoice function is called
        if identify == True:
            print(table1.elchoice(actionchoice))

        # if user input is recognized as molecular formula, weight function is called
        if identify == False:
            print(table1.weight(actionchoice))


main()