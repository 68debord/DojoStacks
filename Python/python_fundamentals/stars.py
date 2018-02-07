
def draw_stars(x): 
	for i in range(0, len(x)):
		if isinstance(x[i], int):
			stars = "*"
			stars *= x[i]
			print stars
		if isinstance(x[i], str):
			stars = (x[i][0]).lower()
			stars *= len(x[i])
			print stars


x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars(x)	
