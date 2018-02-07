class Car(object):
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		self.tax = 0.12
		if price > 10000:
			self.tax = 0.15
		self.display_all()

	def display_all(self):
		print "Price:", self.price
		print "Speed:", self.speed
		print "Fuel:", self.fuel
		print "Mileage:", self.mileage
		print "Tax:", self.tax
		print
		return self

car1 = Car(20000, "40mph", "Full", "300mpg")
car2 = Car(2000, "80mph", "Empty", "57mpg")
car3 = Car(400, "10mph", "Diesel", "20mpg")
car4 = Car(7000, "100mph", "Fullish", "100mpg")
car5 = Car(666, "666mph", "Full", "666mpg")
car6 = Car(1000000, "1000mph", "Electric", "1000mpg")









