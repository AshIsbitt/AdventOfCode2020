# The first step of attacking the weakness in the XMAS data is to find the
# first number in the list (after the preamble) which is not the sum of two of
# the 25 numbers before it. What is the first number that does not have this
# property?

import pytest


def validityChecker(currentVal: int, prevVals: list[int]) -> bool:
    ret: bool = False

    for item in prevVals[-25:]:
        buf = currentVal - item
        if buf in prevVals[-25:] and buf != item:
            ret = True
            break

    return ret


def main(filename: str) -> int:
    with open(filename) as inputFile:
        returnedValues = inputFile.readlines()

    dataValues = list(map(int, returnedValues))

    previousNums = [datum for datum in dataValues[:25]]

    for item in dataValues[25:]:
        isValid = validityChecker(item, previousNums)

        if isValid == True:
            previousNums.append(item)
        elif isValid == False:
            print(f"{isValid=}, {item=}")
            print(previousNums[-25:])
            break

    return 0


test_list = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    24,
    25,
]


@pytest.mark.parametrize(
    ("input_list", "input_value", "expected"),
    (
        (test_list, 26, True),
        (test_list, 49, True),
        (test_list, 100, False),
        (test_list, 50, False),
    ),
)
def test(input_list: list[int], input_value: int, expected: bool) -> None:
    assert validityChecker(input_value, input_list) == expected


if __name__ == "__main__":
    raise SystemExit(main("SuppliedInputs/day9.txt"))
