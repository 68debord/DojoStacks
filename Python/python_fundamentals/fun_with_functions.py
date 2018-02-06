# def odd_even():

# 	for i in range(1, 2001):
# 		string = ""

# 		string += "Number is " + str(i) + "."

# 		if i % 2 == 0:
# 			string += " This is an even number."
# 		if i % 2 == 1:
# 			string += " This is an odd number."

# 		print string

# odd_even()

# ~~~~~~

def multiply(a, num):
	b = []
	for i in range(0, len(a)):
		b.append(a[i]*num)

	return b


a = [2,4,5]
b = multiply(a, 3)
print b


def layered_multiples(arr):
	newArr = []
	for i in range(0, len(arr)):
		
		x=[]
		for i in range(0, arr[i]):
			x.append(1)

		newArr.append(x)	

	return newArr	
		

x = layered_multiples(multiply([2,4,5],3))
print x