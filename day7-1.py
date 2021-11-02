# How many bag colours can eventually contain at least one shiny gold bag?


def dictBuilder(line: str) -> dict[str, dict[str, int]]:
    lineList = line.split("bag")

    outerDict = {}
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


def recursiveBagSearch(parsedRules: dict[str, dict[str, int]], colour: str) -> int:
    for k, v in parsedRules.items():
        if colour in v:
            print(k, v)

    # Recursively search the dist key for names
    # Give the func the colour we want to find
    # Search data for that specific colour
    # get bag that contains said colour
    # Keep going until we find a bag that contains nothing


def main(filename: str) -> int:
    with open(filename) as fileInput:
        bagRules = fileInput.readlines()

    parsedRules = {}

    for line in bagRules:
        parsedRules.update(dictBuilder(line))

    recursiveBagSearch(parsedRules, "shiny gold")

    # for key,value  in parsedRules.items():
    #    if 'shiny gold' in key:
    #        print(key, value)


if __name__ == "__main__":
    raise SystemExit(main("SuppliedInputs/day7.txt"))
