def findChar(list, char):

	new_list = []

	for i in range(0, len(list)):
		if list[i].count(char) > 0:
			new_list.append(list[i])

	print new_list		

findChar(['hello', 'oijff', 'hello'], 'e')