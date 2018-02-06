# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]
# x = students

# def output(x):

# 	for i in x:
# 		print i["first_name"]+" "+i["last_name"] 

# output(x)

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
x = users

def output(x):
 	for key, data in x.items():
 		num = 1
 		print key
 		for value in data:
 			print str(num)+" - "+value["first_name"].upper()+" "+value["last_name"].upper()+" - "+str(len(value["first_name"]+value["last_name"]))
 			num += 1
output(x)