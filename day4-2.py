# In your batch file, how many passports are valid.
import re


def validatePassport(passport: dict[int, int]) -> bool:
    hexaPattern = re.compile(r"#[0-9a-fA-F]")

    if len(passport) != 8 and not (len(passport) == 7 and "cid" not in passport):
        return False
    elif int(passport["byr"]) not in range(1920, 2003):
        return False
    elif int(passport["iyr"]) not in range(2010, 2021):
        return False
    elif int(passport["eyr"]) not in range(2020, 2031):
        return False
    elif passport["hgt"][-2:] not in ["cm", "in"]:
        return False
    elif passport["hgt"][-2:] == "cm" and (
        int(passport["hgt"][:-2]) not in range(150, 194)
    ):
        return False
    elif passport["hgt"][-2:] == "in" and (
        int(passport["hgt"][:-2]) not in range(59, 77)
    ):
        return False
    elif len(passport["hcl"]) != 7 and not re.search(hexaPattern, passport["hcl"]):
        return False
    elif passport["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False
    elif len(passport["pid"]) != 9 or not passport["pid"].isdigit():
        return False
    else:
        return True


def passportCheck(filename: str) -> str:
    with open(filename, "r") as InputFile:
        batchData = InputFile.readlines()

    passports = []
    passport = {}
    validPassportsCount = 0
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

    # Remove empty passports
    passports = [p for p in passports if len(p) > 0]

    # Check each passport dict for length based on valid criteria
    for passport in passports:
        validPassport = validatePassport(passport)
        if validPassport:
            validPassportsCount += 1
        elif validPassport is None:
            print(f"NONE: {passport}")

    return f"{validPassportsCount=}"


print(passportCheck("SuppliedInputs/day4.txt"))
