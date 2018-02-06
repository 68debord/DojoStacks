def foobar(min, max):

	for num in range(min, max):
		is_prime = primality(num)
		is_root = rooter(num)

		if is_prime == True:
			print "Foo"
			continue
		if is_root == True:
			print "Bar"
			continue

		print "Foobar"

def primality(num):
	for i in range(2, num):
		if num % i == 0:
			return False
	return True

def rooter(num):
	for i in range(2, num):
		if i * i == num:
			return True
	return False

		 
foobar(10, 20)


