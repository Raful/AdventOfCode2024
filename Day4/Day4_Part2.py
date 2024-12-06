def is_match(inputData, x, y, expected):
	return y >= 0 and y < len(inputData) and x >= 0 and x < len(inputData[y]) and inputData[y][x] == expected


inputFile = open("Day4_Input.txt", "r")
inputData = inputFile.readlines()

search_word = "MAS"


xmas_count = 0

for y in range(len(inputData)):
	for x in range(len(inputData[y])):
		xmas_found = True
		for i in range(-1, 2):
			if not is_match(inputData, x - i, y - i, search_word[i]):
				xmas_found = False

		if (xmas_found):
			xmas_count += 1

for y in range(len(inputData)):
	for x in range(len(inputData[y])):
		xmas_found = True
		for i in range(-1, 2):
			if not is_match(inputData, x - i, y + i, search_word[i]):
				xmas_found = False

		if (xmas_found):
			xmas_count += 1

for y in range(len(inputData)):
	for x in range(len(inputData[y])):
		xmas_found = True
		for i in range(-1, 2):
			if not is_match(inputData, x + i, y - i, search_word[i]):
				xmas_found = False

		if (xmas_found):
			xmas_count += 1

for y in range(len(inputData)):
	for x in range(len(inputData[y])):
		xmas_found = True
		for i in range(-1, 2):
			if not is_match(inputData, x + i, y + i, search_word[i]):
				xmas_found = False

		if (xmas_found):
			xmas_count += 1

print(xmas_count)

#1482 low