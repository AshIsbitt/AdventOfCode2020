# How many bag colours can eventually contain at least one shiny gold bag? 

def main(filename):
    # Import file as usual
    from open(filename) as file:
        bagRules = file.readlines()

    # For each line, check if they can contain gold
        # If so, add to a dict with a count
        # ex: {light red: 3} means light red bags can contain 3 shiny gold bags
    # Recursively check this (IE if a dark blue bag contains 2 light red bags
    # Then it can hold 6 gold bags)

    # Increment a counter based on if a bag can contain shiny gold
    # Return incrementer

if __name__ == '__main__':
    raise SystemExit(main())
