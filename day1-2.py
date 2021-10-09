# What is the product of the three entries that sum to 2020
# Three-sum problem

def threeSum(filename, sumValue):
	# Import the file with numbers
	with open(filename, 'r') as inputFile:
		numberList = inputFile.readlines()

	# Convert to set for searching speed calcs
	numberSet = set(map(int, numberList))

	print(f"Searching for {sumValue} in 3 numbers")

	#Search for 2020-(x+y) in two loops
	for iterable in numberSet:
		for secondIter in numberSet:

			remaining = (2020 - (iterable + secondIter))

			if remaining <= 0:
				continue
			elif remaining in numberSet:
					return f"""{iterable=}, {secondIter=}, {remaining=}, Product={
					iterable * secondIter * remaining}"""

print(threeSum("SuppliedInputs/day1-1.txt", 2020))
