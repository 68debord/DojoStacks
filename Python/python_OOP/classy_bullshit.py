class User(object):
	pass
~
class ClassName(object):
	#attributes and methods here
~
michael = User()
anna = User()
~
#declare a class and give it name User
class User(object):
	#the __init__ method is called every time a new object is created
	def __init__(self, name, email):
		#set some instance variables. just like any variable we can call these anything
		self.name = name
		self.email = email
		self.logged = False
	#this is a method to help a user login
	def login(self):
		self.logged = True
		print self.name + "is logged in."
		return self
#now create an instance of the class
new_user = User("Anna", "anna@anna.com")
print new_user.email
copy
~

#when we call methods (functions within the object) we don't have to pass in any arguments
#this is known as implicit passage of self
#without self, every time we changed one object's attributes, we'd change the attribute
#for all items of that type
~
#because we know that the init metho will run immediately, we can pass in some parameters
#to that init method upon object creation
#in the init method we are assigning the values we PASSED IN to the values OF THE ATTRIBUTES
#of each individual object
~
#u can chain methods
user1.login().show().logout()
#each method has to return self at the end in order to allow this chaining
~~
class Parent(object): # inherits from the object class
  # parent methods and attributes here
class Child(Parent): #inherits from Parent class so we define Parent as the first parameter
  # parent methods and attributes are implicitly inherited
  # child methods and attributes
  ~
  





