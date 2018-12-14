# Partner 1: Anjali
# Partner 2: Sonali
''' Instructions:
   Work with a partner to complete these tasks. Assume that all variables are declared; you need only write the if-statement using the variables indicated in the description. Write your solution below the commented description.
'''
 
''' 1. 
   Variable grade is a character. If it is an A, print good work. 
'''
grade = "A" # or any other character
if grade == "A":
   print("good work")

 
''' 2. 
   Variable yards is an int. If it is less than 17, multiply yards by 2. 
'''
yards = 5
if yards < 17:
   yards = yards * 2
print(yards)
 
 
 
''' 3. 
   Variable success is a boolean. If something is a success, print congratulations. 
'''
success = True
if success:
   print("Congratulations!")
 
''' 4. 
   Variable word is a String. If the string's second letter is 'f', print fun. 
'''
word = "Hello"
if word[1] == "f":
   print("fun")
 
 
''' 5. 
   Variable temp is a float. Variable celsius is a boolean. If celsius is true, convert to fahrenheit, storing the result in temp. F = 1.8C + 32.
'''
temp = 5.0
celsius = True
if celsius:
   temp = 1.8*temp + 32
print(temp)
 
 
''' 6. 
   Variable numItems is an int. Variable averageCost and totalCost are floats. If there are items, calculate the average cost. If there are no items, print no items.
'''
numItems = 10
averageCost = 0.0
totalCost = 10.0
if numItems == 0:
  print("No items.")
if numItems >0:
   averageCost = numItems/totalCost
   print(averageCost)

 
 
''' 7. 
   Variable pollution is a float. Variable cutoff is a float. If pollution is less than the cutoff, print safe condition. If pollution is greater than or equal to cutoff, print unsafe condition. 
'''
pollution = 6.66
cutoff = 4.20
if pollution < cutoff:
   print("safe condition")
elif pollution >= cutoff:
   print("unsafe condition")

 
''' 8. 
   Variable score is a float, and grade is a char. Store the appropriate letter grade in the grade variable according to this chart.
   F: <60; B: 80-89; D: 60-69; A: 90-100; C: 70-79.
'''
score = 78
grade = "A"

if score < 60:
   grade = "F"
elif score < 70:
   grade = "D"
elif score < 80:
   grade = "C"
elif score < 90:
   grade = "B"
elif score <= 100:
   grade = "A" 

print(grade)

 
''' 9. 
   Variable letter is a char. If it is a lowercase letter, print lowercase. If it is an uppercase, print uppercase. If it is 0-9, print digit. If it is none of these, print symbol.
'''
letter = 'a'
if letter.islower() == True:
   print("lowercase")
elif letter.isupper() == True:
   print("uppercase")
elif letter.isdigit() == True:
   print("digit")
else:
   print("symbol")
 
 
''' 10. 
   Variable neighbors is an int. Determine where you live based on your neighbors.
   50+: city; 25+: suburbia; 1+: rural; 0: middle of nowhere. 
'''
neighbors = 10
location = "location"
if neighbors>=50:
   location = "city"
elif neighbors>=25:
   location = "suburbia"
elif neighbors >=1:
   location = "rural"
else:
   location = "middle of nowhere"
print("Your location is: " + location)
#if neig
 
 
''' 11. 
   Variables doesSignificantWork, makesBreakthrough, and nobelPrizeCandidate are booleans. A nobel prize winner does significant work and makes a break through. Store true in nobelPrizeCandidate if they merit the award and false if they don't. 
'''
doesSignificantWork = True
makesBreakthrough = True
if doesSignificantWork and makesBreakthrough:
   nobelPrizeCandidate = True
else:
   nobelPrizeCandidate = False 
 
 
''' 12. 
   Variable tax is a boolean, price and taxRate are floats. If there is tax, update price to reflect the tax you must pay.
'''
tax = True
price = 4.6
taxRate = 15.8

if tax:
   price -= price*taxRate 
   print(price)
 
 
''' 13.  
   Variable word and type are Strings. Determine (not super accurately) what kind of word it is by looking at how it ends. 
   -ly: adverb; -ing; gerund; -s: plural; something else: error   
'''
word = "lovely"
wordtype = "adjective"

if word[(len(word) - 2):] == "ly":
  wordtype = "adverb"
elif word[(len(word) - 3):] == "ing":
  wordtype = "gerund"
elif word[(len(word) - 1):] == "s":
  wordtype = "plural"

print(wordtype)

 
''' 14. 
   If integer variable currentNumber is odd, change its value so that it is now 3 times currentNumber plus 1, otherwise change its value so that it is now half of currentNumber (rounded down when currentNumber is odd). 
'''
currentNumber = 10
if currentNumber % 2 > 0:
   currentNumber = 3*currentNumber + 1
else:
   currentNumber == currentNumber//2
print(currentNumber)
 
''' 15. 
   Assign true to the boolean variable leapYear if the integer variable year is a leap year. (A leap year is a multiple of 4, and if it is a multiple of 100, it must also be a multiple of 400.) 
'''
leapYear = False
year = 2018
if year%4 == 0:
  if year%100 == 0:
    if year%400 == 0:
      leapYear = True
    else:
      leapYear = False
  else:
    leapYear = True
else:
  leapYear = False
 
 
''' 16. 
   Determine the smallest of three ints, a, b and c. Store the smallest one of the three in int result. 
'''
a = 1
b = 2
c = 3
if a < b and a < c:
   result = a
elif b < a and b < c:
   result = b
else:
   result = c
print(result)
 
 
''' 17. 
   If an int, number, is even, a muliple of 5, and in the range of -100 to 100, then it is a special number. Store whether a number is special or not in the boolean variable special. 
'''
number = 10
special = False

if number%2 == 0 and number%5 == 0 and number >= -100 and number <= -100:
  special = True
else:
  special = False
 
 
''' 18. 
   Variable letter is a char. Determine if the character is a vowel or not by storing a letter code in the int variable code.
   a/e/o/u/i: 1; y: -1; everything else: 0
'''
letter = 'a'
vowels = ['a','e','i','o','u']
if letter in vowels:
   intcode = 1
elif letter == 'y':
   intcode = -1
else:
   intcode = 0

print("Code:",intcode)

 
 
''' 19. 
   Given a string dayOfWeek, determine if it is the weekend. Store the result in boolean isWeekend.
'''
weekend = ["Saturday", "Sunday"]
dayofWeek = "Monday"
if dayofWeek in weekend:
   isWeekend = True
else:
   isWeekend = False

print("It is the weekend, T or F?",isWeekend)
 
''' 20. 
   Given a String variable month, store the number of days in the given month in integer variable numDays. 
'''
month = "January"
numDays = 30
thirtydays = ["September, April, June, November"]
if month in thirtydays:
   numDays = 30
elif month == "February":
   numDays = 28
else:
   numDays = 31
print("The month", month, "has", numDays, "days.")
 
 
''' 21. 
   Three integers, angle1, angle2, and angle3, supposedly made a triangle. Store whether the three given angles make a valid triangle in boolean variable validTriangle.
'''
angle1 = 27
angle2 = 89
angle3 = 73
validTriangle = True
if angle1 + angle2 + angle3 == 180:
  validTriangle = True
else:
  validTriangle = False
 
 
''' 22. 
   Given an integer, electricity, determine someone's monthly electric bill, float payment, following the rubric below. 
   First 50 units: 50 cents/unit
   Next 100 units: 75 cents/unit
   Next 100 units: 1.20/unit
   For units above 250: 1.50/unit, plus an additional 20% surcharge.
'''
electricity = 100
if electricity <= 50:
   payment = 0.50*electricity
elif electricity <= 150:
   payment = 25.00 + 0.75*(electricity-50)
elif electricity <= 250:
   payment = 100.000 + 1.20*(electricity-150)
else:
   payment = 1.2*(220.00 + 1.50*(electricity-250))
print("Your electricity payment is", payment, "dollars!")


 
 
''' 23.
   String, greeting, stores a greeting. String language stores the language. If the language is English, greeting is Hello. If the language is French, the greeting is Bonjour. If the language is Spanish, the greeting is Hola. If the language is something else, the greeting is something of your choice.
'''
greeting = "Shalom"
language = "English"
 
if language == "English":
  greeting = "Hello"
elif language == "French":
  greeting = "Bonjour"
elif language == "Spanish":
  greeting = "Hola"
else:
  greeting = "Namaste"
 
 
''' 24. 
   Generate a phrase and store it in String phrase, given an int number and a String noun. Here are some sample phrases:
   number: 5; noun: dog; phrase: 5 dogs
   number: 1; noun: cat; phrase: 1 cat
   number: 0; noun: elephant; phrase: 0 elephants
   number: 3; noun: human; phrase: 3 humans
   number: 1; noun: home; phrase: 3 homes
'''
number = 1
noun = "Computer"
if number == 1:
   phrase = str(number) + " " + noun
else:
   phrase = str(number) + " " + noun + "s"
print(phrase)
  
 
''' 25. 
   If a string, userInput, is bacon, print out, "Why did you type bacon?". If it is not bacon, print out, "I like bacon." 
'''
userInput = "bacon"

if userInput == "bacon":
  print("Why did you type bacon?")
else:
  print("I like bacon.")
 
''' 26.
   Come up with your own creative tasks someone could complete to practice if-statements. Also provide solutions.
'''
 
''' Task 1:
   String variable, month, stores a month. Int variable, day, stores a day. Generate a date and then use if-statements to figure out what season it is. Store the season in string variable, season. Assume that each new season begins on the 21st of the previous season's last month. (Ex; spring would begin on March 21st.)
'''
 
# solution
month = "January"
day = 1
fall = []
if month in ("January, February, March"):
   season = "Winter"
elif month in ("April, May, June"):
   season = "Spring"
elif month in ("July, August, September"):
   season = "Summer"
elif month in ("October, November, December"):
   season = "Fall"

if month == "March" and day>=21:
   season = "Spring"
if month == "June" and day>=21:
   season = "Summer"
if month == "September" and day>=21:
   season = "Fall"
if month == "December" and day>=21:
   season = "Winter"

print(season)

 
''' Task 2:
  Keep track of textbooks you have bought in the school store. Integer textbooks keeps track of the number of textbooks bought. Float money shows the number of dollars in your Choate account. Boolean buy keeps track of if you are buying textbooks. Every time you buy a textbook, the number of textbooks go up by 1 and the amount of money in your account goes down by $100. 
'''

# solution
textbooks = 5
money = 1000
while True:
  user = input("Would you like to buy a textbook? Enter yes, no, or quit.\n>>")
  if user.lower() == "yes":
    textbook = True
  elif user.lower() == "no":
    textbook = False
  else:
    quit()
  if textbook and money>=100:
    print("You bought a textbook!")
    textbooks +=1
    money -=100
    print("You now have", textbooks, "textbook(s). The amount of money left in your bank account is:", money, "dollars.")
  else:
    print("You didn't buy a textbook. You have", money,"dollars in your bank account.")

 
 
 
''' Task 3: Make sure you are driving safe. Integer speedLimit stores the speed limit. integer carSpeed stores your car's speed. If your car is driving unsafely print "You are driving unsafely. Please slow down". If your car is driving safely print "You are driving safely."
 
'''
 
# solution
speedLimit = 50
carSpeed = 51
if carSpeed > speedLimit:
  print("You are driving unsafely. Please slow down.")
else:
  print("You are driving safely.")
 


''' Sources
 http://www.bowdoin.edu/~ltoma/teaching/cs107/spring05/Lectures/allif.pdf
 http://www.codeforwin.in/2015/05/if-else-programming-practice.html
 Ben Dreier for pointing out some creative boolean solutions.
'''