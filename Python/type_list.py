def typeList(input):
	string = ''
	sum = 0
	intBoo = False
	stringBoo = False

	for i in range(0, len(input)):

		if isinstance(input[i], int):
			intBoo = True
			sum += input[i]

		if isinstance(input[i], str):
			stringBoo = True
			string += input[i]


	if intBoo == True and stringBoo == False:
		print "The list you entered is of integer type"

	if intBoo == False and stringBoo == True:
		print "The list you entered is of string type"

	if intBoo == True and stringBoo == True:
		print "The list you entered is of mixed type"

	print "String: " + string
	print "Sum: " + str(sum)

typeList([44, "hello", 55, "world", 99])


