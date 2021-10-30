# Find the two entries that sum up to 2020; what do you get if you multiply them together?


def findNumsEqualToSumAndReturnProduct(filename, sumValue):
    # Import the file with numbers
    with open(filename, "r") as inputFile:
        numberList = inputFile.readlines()

    print(f"Searching for {sumValue}")
    for numbers in range(len(numberList)):
        currentFirstNum = int(numberList[numbers])
        secondNum = 0

        print(f"Iterating through {currentFirstNum}")

        for iterable in range(len(numberList)):
            # print(f"{numberList[iterable]}")
            if (int(numberList[iterable]) + currentFirstNum) == sumValue:
                secondNum = int(numberList[iterable])
                print("*****FOUND IT*****")
                break

        if secondNum != 0:
            break

    return f"{currentFirstNum=}, {secondNum=}, Total={currentFirstNum*secondNum}"


print(findNumsEqualToSumAndReturnProduct("SuppliedInputs/day1-1.txt", 2020))
