# In your batch file, how many passports are valid.
# https://dev.to/aspittel/comment/18mb0


def passportCheck(filename: str) -> str:
    with open(filename, "r") as InputFile:
        batchData = InputFile.readlines()

    passports = []
    passport = {}
    validPassports = 0
    tempLine = ""

    for line in batchData:
        # Split non-empty lines to individual dicts
        if line != "\n":
            tempLine += str(line)

        if line == "\n":
            tempLine = tempLine.replace("\n", " ")
            tempfield = tempLine.rstrip().split(" ")
            tempfield = [field.split(":") for field in tempfield]
            tempLine = ""

            for field in tempfield:
                passport[field[0]] = field[1]

        # Store passport dict into passports list
        passports.append(passport)
        passport = {}

    # Check each passport dict for length based on valid criteria
    for passport in passports:
        if len(passport) == 8:
            validPassports += 1
        elif (len(passport) == 7) and ("cid" not in passport):
            validPassports += 1

    return f"{validPassports=}"


print(passportCheck("SuppliedInputs/day4.txt"))
