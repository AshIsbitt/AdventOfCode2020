# How many bag colours can eventually contain at least one shiny gold bag?


def main(filename):
    # Import file as usual
    with open(filename) as fileInput:
        bagRules = fileInputs.readlines()

    # For each line, check if they can contain gold
    # If so, add to list in dict
    # {gold: {red: 2, blue: 3, green: 2}}
    # In this ex, there are 2 gold bags in a red bag, and 3 in a blue bag

    # for each key(colour) in dict, count how many gold bags they can contain
    # based off of other dict entries too

    # Increment a counter based on if a bag can contain shiny gold
    # Return incrementer


if __name__ == "__main__":
    raise SystemExit(main("SuppliedInputs/day7.txt"))
