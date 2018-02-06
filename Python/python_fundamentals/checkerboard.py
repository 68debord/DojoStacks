def checkers(stars, height):
	string = ""

	for i in range(0, stars):
		string += "* "

	for i in range(0, height):
		if i % 2 == 0:
			print string
		else:
			print " " + string

checkers(20, 20)