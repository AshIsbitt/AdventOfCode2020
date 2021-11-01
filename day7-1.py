# How many bag colours can eventually contain at least one shiny gold bag?


def dictBuilder(line):
    lineList = line.split("bag")

    outerDict = {}

    for item in lineList:
        innerDict = {}
        item = item.rstrip(".\n, ")
        item = item.lstrip(", scontain")
        # item = 2 light brown

        try:
            innerDict[item[2:]] = int(item[0])
            # {color:val}
        except:
            continue

        outerDict.update(innerDict)
        # {color: {color:val, color:val}}
    return outerDict


def main(filename):
    with open(filename) as fileInput:
        bagRules = fileInput.readlines()

    parsedRules = {}

    for line in bagRules:
        parsedRules.update(dictBuilder(line))

    print(parsedRules)

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
