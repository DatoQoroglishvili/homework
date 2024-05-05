#In Python a function is defined using the def keyword
def my_function():
  print("Hello from a function")
#To call a function, use the function name followed by parenthesis
def my_function():
  print("Hello from a function")

my_function()
#examplers
def my_function(fname):
  print(fname + " Refsnes")
my_function("dato")
my_function("alex")
my_function("mate")

#This function expects 2 arguments, and gets 2 arguments

def my_function(fname, lname):
  print(fname + " " + lname)
my_function("Emil", "Refsnes")

#If the number of arguments is unknown, add a * before the parameter name

def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("dato", "mate", "ALEX")

#You can also send arguments with the key = value syntax.
#This way the order of the arguments does not matter.

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "dato", child2 = "mate", child3 = "alex")

#If the number of keyword arguments is unknown, add a double ** before the parameter name

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

#If we call the function without argument, it uses the default value

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#To let a function return a value, use the return statement:

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

#To specify that a function can have only positional arguments, add , / after the arguments:

def my_function(x, /):
  print(x)

my_function(3)

#Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments:

def my_function(x):
  print(x)

my_function(x = 3)
