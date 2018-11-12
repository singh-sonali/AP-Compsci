# Sonali Singh and Anjali Mangla
# November 12, 2018
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

    # ansi escape codes change color of text
    print("\033[3;34;48mWelcome to the Periodic Table Mastery Chart! This program is designed to help the user with chemistry homework and become well-equipped with the elements.\033[0;30;48m\n")

    while True:

    	# ansi escape codes change color of text
        actionchoice = input("\n\033[1;35;48mEnter an element name, symbol, or molecular formula to access information. \033[0;36;48m\n(enter Q to quit)\033[0;30;48m\n>> ")

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