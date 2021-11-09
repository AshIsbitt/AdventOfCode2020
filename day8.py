# Immediatly before any instruction is executed a second time, what value is in
# the accumulator
# pt2: Fix the program so that it terminates normally by changing exactly one
# NOP to JMP or reverse. What is the value of the accumulator after the program
# terminates.


def bufChecker(
    bufHistory: list[int], instruction: tuple[int, str]
) -> tuple[bool, list[int]]:
    instructionPointer = instruction[0]

    if instructionPointer in bufHistory:
        return True, bufHistory
    else:
        return False, bufHistory


def checkInterpretation(numOfInstructionsRun: int, instructionSet: list[str]) -> bool:
    if numOfInstructionsRun != len(instructionSet):
        return False
    else:
        return True


def attemptedRepair(
    instructionSet: list[str], changedIndex: int
) -> tuple[list[str], int]:

    for index, instruction in enumerate(instructionSet):
        if index <= changedIndex:
            continue
        if instruction[:3] == "jmp":  # and instruction[4] == '-':
            instruction = instruction.replace("jmp", "nop")
            print(f"{instruction=}")
            changedIndex = index
            break
        elif instruction[:3] == "nop":
            instruction = instruction.replace("nop", "jmp")
            print(f"{instruction=}")
            changedIndex = index
            break

    return instructionSet, changedIndex


def interpreter(instructionSet: list[str]) -> tuple[int, int]:
    accumulator: int = 0
    bufHistory: list[int] = []
    pointer: int = 0

    instructionsWithPointers: list[tuple[int, str]] = [
        (i, v.rstrip()) for i, v in enumerate(instructionSet)
    ]

    while True:
        instruction: tuple[int, str] = instructionsWithPointers[pointer]

        """print(
            f"Pointer: {pointer},",
            f"instruction: {instruction},",
            f"accumulator: {accumulator}",
        )"""

        alreadyExecuted, bufHistory = bufChecker(bufHistory, instruction)

        if alreadyExecuted == True:
            return accumulator, len(bufHistory)
        else:
            bufHistory.append(instruction[0])

        if instruction[0] == len(instructionSet) + 1:
            print("Program terminated successfully")
            return accumulator, len(bufHistory)

        if instruction[1][:3] == "jmp":
            pointer += int(instruction[1][4:])
            if pointer < 0:
                pointer == 0
        else:
            pointer += 1
            if instruction[1][:3] == "acc":
                accumulator += int(instruction[1][4:])


def main(filename: str) -> int:
    with open(filename) as rawInstructions:
        instructionSet = rawInstructions.readlines()

    changedIndex: int = 0
    hasTerminatedSuccessfully: bool = False

    while not hasTerminatedSuccessfully:
        instructionSet, changedIndex = attemptedRepair(instructionSet, changedIndex)
        print(f"Testing instruction set with {changedIndex=} changed")

        accumulator, numOfInstructionsRun = interpreter(instructionSet)
        hasTerminatedSuccessfully = checkInterpretation(
            numOfInstructionsRun, instructionSet
        )

        if hasTerminatedSuccessfully:
            break
        elif changedIndex == 635:
            hasTerminatedSuccessfully == True
            break

    print(f"{accumulator=}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main("SuppliedInputs/day8.txt"))
