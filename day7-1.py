# How many bag colours can eventually contain at least one shiny gold bag?


def dictBuilder(line: str) -> dict[str, dict[str, int]]:
    lineList = line.split("bag")

    outerDict: dict[str, dict[str, int]] = {}
    outerDict[lineList[0]] = {}

    for item in lineList:
        innerDict = {}
        item = item.rstrip(".\n, ")
        item = item.lstrip(", scontain")

        try:
            innerDict[item[2:]] = int(item[0])
        except Exception:
            continue

        outerDict[lineList[0]].update(innerDict)

    return outerDict


def recursiveBagSearch(
    parsedRules: dict[str, dict[str, int]], colour: str
) -> list[str]:
    verifiedColours: list[str] = []

    for key, value in parsedRules.items():
        if colour in value:
            verifiedColours.append(key[:-1])
            # print(f"{key=} contains {colour}")

    for searchColour in verifiedColours:
        verifiedColours += recursiveBagSearch(parsedRules, searchColour)

    verifiedColours = list(dict.fromkeys(verifiedColours))
    return verifiedColours


def main(filename: str) -> int:
    with open(filename) as fileInput:
        bagRules = fileInput.readlines()

    parsedRules = {}

    for line in bagRules:
        parsedRules.update(dictBuilder(line))

    colours = recursiveBagSearch(parsedRules, "shiny gold")
    print(len(colours))
    return 0


if __name__ == "__main__":
    raise SystemExit(main("SuppliedInputs/day7.txt"))
