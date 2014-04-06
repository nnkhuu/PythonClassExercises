# Challenge level: Beginner

# Goal: Using the code from Lesson 3: File handling and dictionaries, create a function that will open a CSV file and return the result as a nested list.

def csv_open(filename):
	with open(filename, "r") as csv_file:
		csv=csv_file.read()
	
	return csv

print csv_open("states.csv")
print csv_open("nancy_movies.csv")
