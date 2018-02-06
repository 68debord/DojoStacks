
myDict = {"name": "Nollid", "age": "666", "country of birth": "USA", "favorite language": "Japanese"}
x = myDict

def dictPrinter(x):
	for key,data in x.items():
		print "My "+key+" is "+data

dictPrinter(x)

#learned that dictionaries don't function like lists and thus don't print in any specific order
