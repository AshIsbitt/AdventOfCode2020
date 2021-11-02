# What is the highest seat ID on a boarding plane?
# Binary tree searching

# Convert the input into binary number
def seatParser(line:str) -> int:
	binaryString = ''

	for char in line:
		match char:
			case 'F':
				binaryString += '0'
			case 'B':
				binaryString += '1'
			case 'L':
				binaryString += '0'
			case 'R':
				binaryString += '1'

	binaryNum = int(binaryString, 2)

	return binaryNum


def main(filename:str) -> int:
	with open(filename, 'r') as fileInput:
		batchData = fileInput.readlines()

	seatIDArray = []

	for line in batchData:
		seatIDArray.append(seatParser(line))

	return max(seatIDArray)

if __name__ == '__main__':
	print(main('SuppliedInputs/day5.txt'))
