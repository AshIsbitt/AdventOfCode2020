# Immediatly before any instruction is executed a second time, what value is in
# the accumulator


def bufChecker(
    bufHistory: list[int], instruction: list[int, str]
) -> tuple[bool, list[int]]:
    instructionPointer = instruction[0]

    if instructionPointer in bufHistory:
        return True, bufHistory
    else:
        return False, bufHistory


def interpreter(instructionSet: list[str]) -> int:
    accumulator: int = 0
    bufHistory: list[int] = []
    pointer: int = 0

    instructionsWithPointers = tuple(enumerate(instructionSet))

    while True:
        instruction = list(instructionsWithPointers[pointer])
        instruction[1] = instruction[1].rstrip()

        print(
            f"Pointer: {pointer},",
            f"instruction: {instruction},",
            f"accumulator: {accumulator}",
        )

        alreadyExecuted, bufHistory = bufChecker(bufHistory, instruction)

        print(f"{alreadyExecuted=}")
        if alreadyExecuted == True:
            return accumulator
        else:
            bufHistory.append(instruction[0])

        if instruction[1][:3] == "jmp":
            pointer += int(instruction[1][4:])
        else:
            pointer += 1
            if instruction[1][:3] == "acc":
                accumulator += int(instruction[1][4:])


def main(filename: str) -> int:
    with open(filename) as rawInstructions:
        instructionSet = rawInstructions.readlines()

    accumulator = interpreter(instructionSet)

    print(f"{accumulator=}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main("SuppliedInputs/day8.txt"))
