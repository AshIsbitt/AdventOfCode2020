# Find a chain that uses all of your adapters to connect the charging outlet to
# your device's built-in adapter and count the joltage differences between the
# charging outlet, the adapters, and your device. What is the number of 1-jolt
# differences multiplied by the number of 3-jolt differences?
import pytest


def main(filename: str) -> int:
    with open(filename) as inputFile:
        adapterData = inputFile.readlines()

    return 0


if __name__ == "__main__":
    raise SystemExit(main("SuppliedInputs/day10.txt"))


test_data == []
