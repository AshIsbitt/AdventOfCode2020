# How many individual bags are required inside your single shiny gold bag?


def dictBuilder(line: str) -> dict[str, dict[str, int]]:
    lineList = line.split("bag")
    lineList[0] = lineList[0].rstrip()

    outerDict: dict[str, dict[str, int]] = {}
    outerDict[lineList[0]] = {}

    for item in lineList:
        innerDict = {}
        item = item.rstrip(".\n, ")
        item = item.lstrip(", scontain")

        try:
            innerDict[item[2:]] = int(item[0])
        except:
            continue

        outerDict[lineList[0]].update(innerDict)

    return outerDict


def recursiveBagContainers(
    parsedRules: dict[str, dict[str, int]], entryPoint: str
) -> int:
    totalBags: int = 0

    for colour, quantity in parsedRules[entryPoint].items():
        totalBags += quantity * (recursiveBagContainers(parsedRules, colour) + 1)

    return totalBags


def main(filename: str) -> int:
    with open(filename) as fileInput:
        bagRules = fileInput.readlines()

    parsedRules = {}

    for line in bagRules:
        parsedRules.update(dictBuilder(line))

    bagsInShinyGold = recursiveBagContainers(parsedRules, "shiny gold")
    print(bagsInShinyGold)
    return 0


if __name__ == "__main__":
    raise SystemExit(main("SuppliedInputs/day7.txt"))
