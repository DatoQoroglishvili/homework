#A variable is created the moment you first assign a value to it.
#examples
x = 5
y = "dato"
print(x)
print(y)


x = str(3)
y = int(3)
z = float(3)
# x will be '3'
# y will be 3
# z will be 3.0

#Get the Type
#You can get the data type of a variable with the type() function.
x = 5
y = "John"
print(type(x)) #class int
print(type(y)) #class str

#Case-Sensitive
#This will create two variables:
a = 4
A = "Sally"
print(a)
print(A)
# A and a is not the same to use

#Variable Names
#Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)
#It will print john because we use diffirent variable names

#Many Values to Multiple Variables
#Python allows you to assign values to multiple variables in one line
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#you can assign the same value to multiple variables in one line:
x = y = z = "Orange"
print(x)
print(y)
print(z)
#it will print orange 3 times because of same value to multiple variables

#Unpack a list:
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Python - Output Variables

#Output Variables
#The Python print() function is often used to output variables.
x = "Python is awesome"
print(x)

#In the print() function, you output multiple variables, separated by a comma:
x = "Python"
y = "is"
z = "awesome"
print(x, y, z) #you can use , and + to

#For numbers, the + character works as a mathematical operator:
x = 5
y = 10
print(x + y)#ist like write 5+10=15
#you cant combine str and number with + bc it will be error

#Global Variables
#Create a variable outside of a function, and use it inside the function

x = "awesome"
def myfunc():
  print("Python is " + x)

myfunc()
# with this it will print that python is awesome

#Create a variable inside a function, with the same name as the global variable
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#The global Keyword
#To create a global variable inside a function, you can use the global keyword.
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)