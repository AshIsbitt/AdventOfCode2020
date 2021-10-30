# What do you get if you multiply together the number of trees encountered on each of the listed
# slopes


def treeMapDetector(filename, rightPattern, downPattern):
    with open(filename, "r") as inputFile:
        tobogganMap = inputFile.readlines()

    tobogganMapArray = list(map(list, tobogganMap))
    treeCounter = 0
    iterator = 0

    for line in tobogganMapArray[::downPattern]:
        line.remove("\n")

        if iterator >= len(line):
            iterator -= len(line)

        if line[iterator] == "#":
            treeCounter += 1

        iterator += rightPattern

    return treeCounter


filePath = "SuppliedInputs/day3.txt"
print(f"Right 1, down 1 = {treeMapDetector(filePath, 1, 1)}")
print(f"Right 3, down 1 = {treeMapDetector(filePath, 3, 1)}")
print(f"Right 5, down 1 = {treeMapDetector(filePath, 5, 1)}")
print(f"Right 7, down 1 = {treeMapDetector(filePath, 7, 1)}")
print(f"Right 1, down 2 = {treeMapDetector(filePath, 1, 2)}")

print(
    f"""Total sum = {treeMapDetector(filePath, 1, 1) * treeMapDetector(filePath, 3, 1) *
treeMapDetector(filePath, 5, 1) * treeMapDetector(filePath, 7, 1) *
treeMapDetector(filePath, 1, 2)}"""
)
