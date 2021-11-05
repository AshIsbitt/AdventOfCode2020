# Immediatly before any instruction is executed a second time, what value is in
# the accumulator


def main(filename: str) -> int:
    with open(filename) as rawInstructions:
        instructionSet = rawInstructions.readlines()

    accumulator: int = 0
    instructionHistory: set[int] = set()
    pointer: int = 0

    while True:
        print(f"Index: {pointer}, instruction: {instructionSet[pointer]}")

        if pointer in instructionHistory:
            break
        else:
            # This is wrong - need to think about getting pointer as the index
            # of the list and manipulating that to get the individual
            # instructions
            instructionHistory = {*(pointer)}

        if instruction[:3] == "jmp":
            index += int(instruction[4:])
        elif instruction[:3] == "acc":
            accumulator += int(instruction[4:])
        elif instruction[:3] == "nop":
            continue

        pointer

    print(f"{accumulator=}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main("SuppliedInputs/day8.txt"))
