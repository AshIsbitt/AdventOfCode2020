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
        if buf in prevVals[-25:]:  # and buf != item:
            ret = True
            break

    return ret


def locateAnomalousValue(returnedValues: list[str]) -> int:
    dataValues = list(map(int, returnedValues))

    previousNums = dataValues[:25]
    # print(f'{dataValues.index(135559)=}')

    for item in dataValues[25:]:
        isValid = validityChecker(item, previousNums)

        if isValid == True:
            previousNums.append(item)
        else:
            break

    return item


def main(filename: str) -> int:
    with open(filename) as inputFile:
        returnedValues = inputFile.readlines()

    anomalousValue = locateAnomalousValue(returnedValues)
    print(f"Part 1: {anomalousValue=}")

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


if __name__ == "__main__":
    raise SystemExit(main("SuppliedInputs/day9.txt"))
