# How many passwords are valid according to their policies?

# open file
with open("SuppliedInputs/day2.txt", "r") as inputFile:
    passwordList = [s.strip() for s in inputFile.readlines()]

validPasswordCounter = 0

for line in passwordList:
    range, policy, sample = line.split(" ")
    lower, higher = range.split("-")

    numOfPolicyChar = 0

    for char in sample:
        if char == policy[0]:
            numOfPolicyChar += 1

    if numOfPolicyChar <= int(higher) and numOfPolicyChar >= int(lower):
        validPasswordCounter += 1

print(f"{validPasswordCounter=}")
