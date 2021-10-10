# How many passwords are valid according to the new interpretation of their policy?

with open("SuppliedInputs/day2.txt", 'r') as inputFile:
	passwordList = [s.strip() for s in inputFile.readlines()]

validPasswordCounter = 0

for line in passwordList:
	range, policy, sample = line.split(' ')
	lower, higher = range.split('-')

	numOfPolicyChar = 0

	if bool(sample[int(lower)-1] == policy[0]) != bool(sample[int(higher)-1] == policy[0]):
		validPasswordCounter += 1

print(f"{validPasswordCounter=}")
