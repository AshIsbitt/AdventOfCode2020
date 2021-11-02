# For each group, count the number of questions to which anyone answered 'yes'.
# What is the sum of those counts


def sumOfCounts(customsData: list[str]) -> int:
    sum = 0

    for item in customsData:
        item = [char for char in item if char != "\n"]

        sum += len(set(item))

    return sum


def main(filename: str) -> int:
    with open(filename, "r") as inputFile:
        customsFormData = inputFile.read().split("\n\n")

    return sumOfCounts(customsFormData)


if __name__ == "__main__":
    raise SystemExit(print(main("SuppliedInputs/day6.txt")))
