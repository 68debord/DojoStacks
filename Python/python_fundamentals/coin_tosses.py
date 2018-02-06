import random
def coinThrow(times):
	headSum = 0
	tailSum = 0
	for i in range(1, times+1):
		x = round(random.random())	
		if x == 1:
			result = "head"
			headSum += 1
		if x == 0: 
			result = "tail"
			tailSum += 1			
		print "Attempt #"+str(i)+": Throwing a coin...It's a "+result+"! ... Got "+str(headSum)+" head(s) so far and "+str(tailSum)+" tail(s) so far."
coinThrow(10)