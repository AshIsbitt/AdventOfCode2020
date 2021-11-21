# What is the encryption weakness in your XMAS-encrypted list of numbers?

import pytest


def validityChecker(currentVal: int, prevVals: list[int]) -> bool:
    ret: bool = False

    for item in prevVals[-25:]:
        buf = currentVal - item
        if buf in prevVals[-25:]:  # and buf != item:
            ret = True
            break

    return ret


def dataValidation(returnedValues: list[str]) -> int:
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

    anomalousValue = dataValidation(returnedValues)
    print(f"{anomalousValue=}")

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
def test_validityChecker(
    input_list: list[int], input_value: int, expected: bool
) -> None:
    assert validityChecker(input_value, input_list) == expected


if __name__ == "__main__":
    raise SystemExit(main("SuppliedInputs/day9.txt"))
