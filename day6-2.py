# For each group, count the number of questions to which everyone answered 'yes'. What is the sum
# of those counts

import string


def countAnswers(customsData: str) -> int:
    customsData = customsData.rstrip()
    peopleInGroup = customsData.count("\n") + 1
    groupYesAnswers = ""

    customsData = customsData.replace("\n", "")

    for letter in list(string.ascii_lowercase):
        if customsData.count(letter) == peopleInGroup:
            groupYesAnswers += letter

    return len(groupYesAnswers)


def main(filename: str) -> str:
    with open(filename, "r") as inputFile:
        customsFormData = inputFile.read().split("\n\n")

    sumOfCounts = 0

    for item in customsFormData:
        sumOfCounts += countAnswers(item)

    print(f"{sumOfCounts=}")


if __name__ == "__main__":
    raise SystemExit(main("SuppliedInputs/day6.txt"))
