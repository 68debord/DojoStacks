import random

def scoresGrades(times):
	print "Scores and Grades"
	for i in range(0, times):
		grade = random.randint(60, 100)

		if grade <= 69:
			score = "D"
		if grade >= 70 and grade <= 79:
			score = "C"
		if grade >= 80 and grade <= 89:
			score = "B"
		if grade >= 90:
			score = "A"	

		print "Score: "+str(grade)+"; Your grade is "+score

scoresGrades(10)
