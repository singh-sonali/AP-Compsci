# Sonali Singh and Anjali Mangla
# Jan. 30, 2019
# Some Examples Using NumPy!
import numpy

# showing basic array formations
def basic_operations():
	# Creating regular numpy arrays
	d_array = numpy.array([1, 2, 3, 4, 5, 6]) 
	print("1d array:", d_array)
	dd_array = numpy.array([[1, 2, 3],[4, 5, 6]]) 
	print("2d array:", dd_array)

	# Special 1d array formation methods
	range_array = numpy.arange(0,11,2) # array of values in given range
	print("Range array:", range_array) 

	identity_array = numpy.eye(3) # identity matrix
	print("Identity matrix:", identity_array)

	null_array = numpy.zeros(6) # array of zeroes
	print("Null array:", null_array)

	random_array = numpy.random.rand(6) # random floats
	print("Random float array:", random_array)

	randint_array = numpy.random.randint(0, 10, 6) # random ints
	print("Random int array:", randint_array)

basic_operations()

# showing the vectorization of lists in numpy
def vectorization():
	# Multiplying in numpy vs regular
	reg_array = [1,2,3,4,5]
	num_array = numpy.array([1,2,3,4,5])
	new_array = []

	# Multiply each element in the list by five
	# Regular way
	for element in reg_array:
		new_array.append(5*reg_array[element-1])
	print(new_array)

	# Numpy way
	new_array = 5 * num_array
	print(new_array)

	# Note: any mathematical operation can be done in numpy to every element with just one line. Without numpy, a for loop is needed.

vectorization()

# applications for a fake dataset in numpy
def classroom_application():
	# create random dataset of ages
	class_ages = numpy.random.randint(13, 19, 10)
	# sort ages from smallest to largest
	class_ages = numpy.sort(class_ages)
	print("Class ages:", class_ages)

	# find average of ages
	mean = numpy.mean(class_ages)
	print("Average class age:", mean, "years")

	# find standard deviation in class ages
	std = numpy.std(class_ages)
	print("Standard deviation:", std)

	# find maximum and minimum ages
	max_age = numpy.max(class_ages)
	min_age = numpy.min(class_ages)
	print("Maximum age:", max_age, "years. Minimum age:", min_age, "years.")

	# Alternative options for finding min and max ages using indexing
	max_age = class_ages[0]
	max_age = class_ages[9]


classroom_application()

# showing interactions between two arrays in numpy
def interarray_stuff():
	# Make two different arrays 
	array1 = numpy.arange(1,11,1)
	print("Array 1:", array1)
	array2 = numpy.random.randint(0,20,10)
	print("Array 2:", array2)

	# Create list with all elements isolated to array 2
	just_array2 = numpy.setdiff1d(array2, array1)
	print("Elements isolated to Array 2:", just_array2)

	# Product of two arrays (note: you cannot do this without numpy!)
	product = array1*array2
	print("Products of two arrays:", product)

	# Find all similar elements in arrays
	intersection = numpy.intersect1d(array1, array2)
	print("Similar elements:", intersection)

	# Find dot product of two arrays
	dot_product = numpy.dot(array1,array2)
	print("Dot product:", dot_product)


interarray_stuff()

# applying numpy to real-life math problem
def volume_problem():
	# Problem: You are given 5 cylindrical containers with different radius and heights ranging between 5 and 25 cm. Find out a) the volume of water that each container can contain and b) The maximum volume of water of the cylinders.

	# First step: generate values for radius and height of five cylinders. This is ten random values between 5 and 25.
	values = numpy.random.randint(5, 26, 10)
	print("The values of all of the radii and heights:",values)

	# Arrange 1d list of values into 2d array with 5 rows, one for each cylinder. Left column will be radius, right will be height.
	dim_cylinders = values.reshape(5,2)
	print("Radii (left) and Heights (right):", dim_cylinders)

	# Separate radius and height for each cylinder to calculate volume, using splicing.
	radius = dim_cylinders[:,0]
	height = dim_cylinders[:,1]

	# Calculate volume using radius and height for each cylinder, and store in new array
	volume = numpy.pi*radius*height
	print("Volumes of five cylinders:",volume)

	# Find position of cylinder with maximum volume (add 1 bc index begins at 0)
	max_cylinder = numpy.argmax(volume)
	print("Cylinder",max_cylinder+1,"has the largest volume.")
	# Find maximum in volume array
	max_vol = numpy.max(volume)
	print("Maximum cylinder volume:", max_vol)


volume_problem()

# OMH: Sonali Singh
# OMH: Anjali Mangla
	

	

