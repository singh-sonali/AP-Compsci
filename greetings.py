#Sonali Singh
#9/10/18
#Source: https://swcarpentry.github.io/python-novice-inflammation/10-cmdline/
import sys 
# if you give too many arguments, it's fine, they're just ignored
#too little arguments gives you an error
# [0] references the name of the file, because it's technically the first argument
name = sys.argv[1]
name2 = sys.argv[2]

#len(sys.argv)
#this tells how many arguments have been passed



print("Hello, " + name + " and " + name2 +"!")