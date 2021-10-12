# In your batch file, how many passports are valid.

def passportCheck(filename):
	with open(filename, 'r') as InputFile:
		batchData = InputFile.readlines()

	passports = []
	passport = {}
	validPassports = 0
	tempLine = ""

	for line in batchData:
		# Split non-empty lines to individual dicts
		if line != '\n':
			tempLine += line
			tempLine += ' '

		if line == '\n':
			line = tempLine.rstrip().split(' ')
			line = [field.split(':') for field in line]

			for field in line:
				passport[field[0]] = field[1]
				tempLine = ''
		else:
			passports.append(passport)
			passport = {}
			tempLine = ''


		# Store passport dict into passports list
		passports.append(passport)
		passport = {}

	return passports

	# Check each passport dict for length based on valid criteria
	for passport in passports:
		if len(passport) == 8:
			validPassports += 1
		elif (len(passport) == 7) and ('cid' not in passport):
			validPassports += 1

	return f'{validPassports=}'


print(passportCheck('SuppliedInputs/day4.txt'))
