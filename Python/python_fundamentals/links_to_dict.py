name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

list1 = name
list2 = favorite_animal

def make_dict(list1, list2):
	#hacker challenge~~
	longer = list1
	shorter = list2

	if len(list2) > len(list1):
		longer = list2
		shorter = list1
	#~~

	zipped = zip(longer, shorter)
	new_dict = dict(zipped)

	return new_dict

print make_dict(list1, list2)	