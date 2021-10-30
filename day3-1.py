# Following a slope of right-3 and down-1, how many trees would you encounter


def treeMapDetector(filename, rightPattern, downPattern):
    with open(filename, "r") as inputFile:
        tobogganMap = inputFile.readlines()

    tobogganMapArray = list(map(list, tobogganMap))
    treeCounter = 0
    iterator = 0

    for line in tobogganMapArray:
        line.remove("\n")
        print(line)

        if iterator >= len(line):
            iterator -= len(line)

        print(f"{iterator=}")
        print(f"{line[iterator]=}")

        if line[iterator] == "#":
            treeCounter += 1

        iterator += rightPattern

    return f"{treeCounter=}"


print(f"Right 3, down 1 = {treeMapDetector('SuppliedInputs/day3.txt', 3, 1)}")
