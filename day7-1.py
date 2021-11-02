# How many bag colours can eventually contain at least one shiny gold bag?


def dictBuilder(line):
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


def containsShinyGoldBag(parsedRules):
    pass

    # Reccursively search the dist key for names


def main(filename):
    with open(filename) as fileInput:
        bagRules = fileInput.readlines()

    parsedRules = {}

    for line in bagRules:
        parsedRules.update(dictBuilder(line))

    for key, value in parsedRules.items():
        print(key, value)

    # for key,value  in parsedRules.items():
    #    if 'shiny gold' in key:
    #        print(key, value)

    # For each line, check if they can contain gold
    # If so, add to list in dict
    # {gold: {red: 2, blue: 3, green: 2}}
    # In this ex, there are 2 gold bags in a red bag, and 3 in a blue bag

    # for each key(colour) in dict, count how many gold bags they can contain
    # based off of other dict entries too

    # Increment a counter based on if a bag can contain shiny gold
    # Return incrementer


if __name__ == "__main__":
    raise SystemExit(main("SuppliedInputs/day7.txt"))
