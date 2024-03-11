# 1
for i in range(6, 56, 5):
    print(i-1)

# 2
for i in range(2, 21, 2):
    print(i)

# 3
for i in range(5, 11):
    pasuxi = i * i
    print(f"{i} * {i} = {pasuxi}")

#4
print(input("enter number"))
def fact( n):
  if n>1:
    return n*fact(n-1)
  else:
    return 1.
n=int(input('enter the number'))
print("Factorial of ",n,"is - ", fact(n))


 # 5 ???
    
    

    
#6
for i in range(10, 1, -1):
     print(i)

#7
name=str(input("Please enter your name: "))
if name =="quit":
   print("you are in")
elif name!="quit":
   print("its incorrect")

#8
for i in range(10,21,2):
   print(i)

#9
num =int(input("Please enter positive number: "))
if num >0:
   print("you have written positive number.")
elif num <0:
    (print("you have written negative number."))

#10
for i in range(1, 11):
    print(i*i)