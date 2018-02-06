
def compareLists(listOne, listTwo):
	
	if len(listOne) != len(listTwo):
		print "The lists are not the same"
		return

	for i in range(0, len(listOne)):
		if listOne[i] != listTwo[i]:
			print "The lists are not the same"
			return

	print "The lists are the same"



compareLists([1,2,3,4],[1,2,3,4])
