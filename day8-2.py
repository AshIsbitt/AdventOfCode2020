# pt2: Fix the program so that it terminates normally by changing exactly one
# NOP to JMP or reverse. What is the value of the accumulator after the program
# terminates.


def repairInstructionSet(
    instructionSet: list[str], changedIndex: int
) -> tuple[list[str], int]:

    for index, instruction in enumerate(instructionSet):
        if index <= changedIndex:
            continue
        elif instruction[:3] == "jmp":
            instructionSet[index] = instruction.replace("jmp", "nop")
            changedIndex = index
            break
        elif instruction[:3] == "nop":
            instructionSet[index] = instruction.replace("nop", "jmp")
            changedIndex = index
            break

    return instructionSet, changedIndex


def bufChecker(
    bufHistory: list[int], instruction: tuple[int, str]
) -> tuple[bool, list[int]]:
    instructionPointer = instruction[0]

    if instructionPointer in bufHistory:
        return True, bufHistory
    else:
        return False, bufHistory


def interpreter(instructionSet: list[str]) -> tuple[bool, int]:
    accumulator: int = 0
    bufHistory: list[int] = []
    pointer: int = 0

    instructionsWithPointers: list[tuple[int, str]] = [
        (i, v.rstrip()) for i, v in enumerate(instructionSet)
    ]

    while pointer < len(instructionsWithPointers):
        instruction: tuple[int, str] = instructionsWithPointers[pointer]

        # print(
        #    f"Pointer: {pointer},",
        #    f"instruction: {instruction},",
        #    f"accumulator: {accumulator}",
        # )

        alreadyExecuted, bufHistory = bufChecker(bufHistory, instruction)

        if alreadyExecuted == True:
            return False, accumulator
        else:
            bufHistory.append(instruction[0])

        if instruction[1][:3] == "jmp":
            pointer += int(instruction[1][4:])
        else:
            pointer += 1
            if instruction[1][:3] == "acc":
                accumulator += int(instruction[1][4:])

    return True, accumulator


def main(filename: str) -> int:
    with open(filename) as rawInstructions:
        instructionSet = rawInstructions.readlines()

    changedIndex: int = 0
    successfulExecutionFlag: bool = False

    while not successfulExecutionFlag:
        instructionSet, changedIndex = repairInstructionSet(
            instructionSet, changedIndex
        )
        print(
            f"Repaired instruction: {instructionSet[changedIndex]} "
            f"at index {changedIndex}"
        )

        successfulExecutionFlag, accumulator = interpreter(instructionSet)

        if changedIndex > len(instructionSet):
            break

    if successfulExecutionFlag == True:
        print(f"{accumulator=}")
    else:
        print("Instruction repair failed")

    return 0


if __name__ == "__main__":
    raise SystemExit(main("SuppliedInputs/day8.txt"))
