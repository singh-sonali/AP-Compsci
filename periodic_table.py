import csv
with open('elements.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter = ',')
	line_count = 0
	for row in csv_reader:
		print(f'\t{row[0]} has an atomic number of {row[1]}. Its periodic symbol is {row[2]}, and its atomic weight is {row[3]} g.')