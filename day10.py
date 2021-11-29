# Find a chain that uses all of your adapters to connect the charging outlet to
# your device's built-in adapter and count the joltage differences between the
# charging outlet, the adapters, and your device. What is the number of 1-jolt
# differences multiplied by the number of 3-jolt differences?
import pytest


def joltageChainCalculator() -> tuple[int, int]:
    count_ones: int = 0
    count_threes: int = 0

    return count_ones, count_threes


def main(filename: str) -> int:
    with open(filename) as inputFile:
        adapterData = inputFile.readlines()

    return 0


if __name__ == "__main__":
    raise SystemExit(main("SuppliedInputs/day10.txt"))

################################################################################

test_data = [
    28,
    33,
    18,
    42,
    31,
    14,
    46,
    20,
    48,
    47,
    24,
    23,
    49,
    45,
    19,
    38,
    39,
    11,
    1,
    32,
    25,
    35,
    8,
    17,
    7,
    9,
    4,
    2,
    34,
    10,
    3,
]

test_data_2 = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]


@pytest.mark.parametrize(
    ("input_list", "expected"),
    (
        (test_data, (22, 10)),
        (test_data_2, (7, 5)),
    ),
)
def test_joltageChainCalculator(
    input_list: list[int], expected: tuple[int, int]
) -> None:
    assert joltageChainCalculator(input_list) == expected
