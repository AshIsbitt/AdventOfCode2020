# Part 1:  The first step of attacking the weakness in the XMAS data is to find
# the first number in the list (after the preamble) which is not the sum of two
# of the 25 numbers before it. What is the first number that does not have this
# property?
# Part 2: What is the encryption weakness in your XMAS-encrypted list of
# numbers?
import pytest


def validityChecker(currentVal: int, prevVals: list[int]) -> bool:
    ret: bool = False

    for item in prevVals[-25:]:
        buf = currentVal - item
        if buf in prevVals[-25:] and buf != item:
            ret = True
            break

    return ret


def locateAnomalousValue(dataValues: list[int]) -> int:
    previousNums = dataValues[:25]
    # print(f'{dataValues.index(135559)=}')

    for item in dataValues[25:]:
        isValid = validityChecker(item, previousNums)

        if isValid:
            previousNums.append(item)
        else:
            break

    return item


def encryptionWeakness(contiguousVals: list[int]) -> int:
    return min(contiguousVals) + max(contiguousVals)


def contiguousNumberFinder(value: int, dataValues: list[int]) -> list[int]:
    for itera, num in enumerate(dataValues):
        contiguousVals: list[int] = []
        contiguousVals.append(num)

        for prevNum in list(reversed(dataValues[:itera])):
            if prevNum == num:
                break

            contiguousVals.append(prevNum)

            if value == sum(contiguousVals):
                return list(reversed(contiguousVals))

    return [0, 0]


def main(filename: str) -> int:
    with open(filename) as inputFile:
        returnedValues = inputFile.readlines()

    dataValues = list(map(int, returnedValues))

    anomalousValue = locateAnomalousValue(dataValues)
    print(f"Part 1: {anomalousValue=}")

    invalidNumberSet = contiguousNumberFinder(anomalousValue, dataValues)
    anomalousSum = encryptionWeakness(invalidNumberSet)
    print(f"Part 2: {anomalousSum}")

    return 0


test_list = list(range(1, 26))


@pytest.mark.parametrize(
    ("input_list", "input_value", "expected"),
    (
        (test_list, 26, True),
        (test_list, 49, True),
        (test_list, 100, False),
        (test_list, 50, False),
    ),
)
def test_validityChecker(
    input_list: list[int], input_value: int, expected: bool
) -> None:
    assert validityChecker(input_value, input_list) == expected


test_list_pt2 = [
    35,
    20,
    15,
    25,
    47,
    40,
    62,
    55,
    65,
    95,
    102,
    117,
    150,
    182,
    127,
    219,
    299,
    277,
    309,
    576,
]


@pytest.mark.parametrize(
    ("input_value", "input_list", "output_list"),
    ((127, test_list_pt2, [15, 25, 47, 40]),),
)
def test_contiguousNumberFinder(
    input_value: int, input_list: list[int], output_list: list[int]
) -> None:
    assert contiguousNumberFinder(input_value, input_list) == output_list


if __name__ == "__main__":
    raise SystemExit(main("SuppliedInputs/day9.txt"))
