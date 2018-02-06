def checker(num):
	for i in range(2, num):
		if num % i == 0:
			break

		if i == num-1:
			print "Foo"
			print num
			return
				


	for i in range(2, num):
		if i * i == num:
			print "Bar"
			print num
			return
		if i == num-1:
			print "Foobar"	
			print num

def foobar(min, max):

	for num in range(min, max):
		checker(num)
def foobar(num):

	is_prime = primality(num)
	is_root = rooter(num)

	if is_prime == true:

		return "Foo"
	if is_root == true:

		return "Bar"
		
	return "Foobar"



def primality(num):

def rooter(num):
		 
foobar(100, 1000)

#this is too sloppy, better to create two different functions that return
#and then have 3 if checks for foo, bar, foobar

