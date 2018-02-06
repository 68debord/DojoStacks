

def filterByType(input):
	if isinstance(input, int):

		if input >= 100:
			print "That's a big number!"
		else:
			print "That's a small number!"

	if isinstance(input, str):
		if len(input) >= 50:
			print "Long sentence."
		else:
			print "Short sentence."
	
	if isinstance(input, list):
		if len(input) >= 10:
			print "Big list!"
		else:
			print "Short list."

filterByType()
	