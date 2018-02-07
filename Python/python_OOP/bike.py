class Bike(object):
	def __init__(self, price, max_speed):
		self.info = (price, max_speed)
		self.miles = 0
	def displayInfo(self):
		if self.miles < 0:
			self.miles = 0
		print self.info, self.miles
		return self
	def ride(self):
		print "Riding!"
		self.miles += 10
		return self
	def reverse(self):
		print "Reverse, Reverse!"
		self.miles -= 5
		return self

bike1 = Bike(200, "150mph")
bike2 = Bike(400, "180mph")
bike3 = Bike(600, "200mph")

bike1.ride().ride().ride().reverse().displayInfo()
bike2.ride().ride().reverse().reverse().displayInfo()
bike3.reverse().reverse().reverse().displayInfo()