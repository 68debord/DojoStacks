class Product(object):
	def __init__(self, price, name, weight, brand):
		self.price = price
		self.name = name
		self.weight = weight
		self.brand = brand
		self.status = "FOR SALE"
	def displayInfo(self):
		print "Name:", self.name
		print "Price:", self.price
		print "Weight:", self.weight
		print "Brand:", self.brand
		print "Status:", self.status
		print
		return self
	def sell(self):
		self.status = "SOLD"
		return self
	def addTax(self, decimalTax):
		return self.price + (self.price * decimalTax)
	def returnItem(self, returnStatus):
		if returnStatus == "defective":
			self.status = "DEFECTIVE"
			self.price = 0
		if returnStatus == "in box":
			self.status = "FOR SALE"
		if returnStatus == "opened":
			self.status = "USED"
			self.price = self.price*.8
		return self

item1 = Product(100, "apple", 12, "apple")
item1.displayInfo()