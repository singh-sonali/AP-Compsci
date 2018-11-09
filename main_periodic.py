from elements import Element
from periodic_table import PeriodicTable
import csv
import re

def main():
    table1 = PeriodicTable()
    print("Welcome to the Periodic Table Mastery Chart! This program is designed to help the user with chemistry homework and become well-equipped with the elements.\n")
    while True:
        actionchoice = input("Enter an element name, symbol, or molecular formula to access information. (enter Q to quit)\n>> ")
        
        if actionchoice.upper() == 'Q':
        	print("Bye!")
        	quit()

        identify = table1.recognize(actionchoice)
        if identify == True:
            print(table1.elchoice(actionchoice))
        if identify == False:
            print(table1.weight(actionchoice))




main()