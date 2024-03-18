#1
toy=20
budget=int(input("please enter your budget :"))
if budget>=toy:
    print("you can buy the toy")
else:
    print("you cant buy the toy")

#2
registered_password = "dato2009"
password = input("Please enter your password: ")

while password != registered_password:
    password = input("Please enter your password again: ")
    if password == registered_password:
        print("You have accses on your account")
    else:
        print("You have entered wrong password, please try again")

#3
start = int(input("Please enter starting value: "))
end = int(input("Please enter ending value: "))
step = int(input("Please enter step value: "))

for i in range(start,end,step):
    print(i)
#4
s1 = int(input("Please enter first side: "))
s2 = int(input("Please enter second side: "))
s3 = int(input("Please enter third side: "))


is_valid = (s1 + s2 > s3) and (s2 + s3 > s1) and (s3 + s1 > s2)

while is_valid != True:
    s1 = int(input("Please enter first side: "))
    s2 = int(input("Please enter second side: "))
    s3 = int(input("Please enter third side: "))

    is_valid = s1 + s2 > s3

#5?????
    





#6
operation = input("Please enter operation (+,-,*,/): ")
num1 = int(input("Please enter first number: "))
num2 = int(input("Please enter second number: "))

if operation == '+':
    print(num1 + num2)
elif operation == '-':
    print(num1 - num2)
elif operation == '*':
    print(num1 * num2)
elif operation == '/':
    print(num1 / num2)
else:
    print("operation is not valid")

#7?
    


#8
birth=int(input("enter your birthday time"))
if birth %4 == 0:
  print("ნაკიანი წელია") 
else:
  print("არ არის ნაკიანი წელი")
#9
a = float(input("შეიყვანეთ პირველი კათეტი: "))
b = float(input("შეიყვანეთ მეორე კათეტი: "))

c = (a**2 + b**2) ** 0.5
print("ჰიპოტენუზა არის:", c)       
#10
age=int(input("enter your age:"))
if age>=18:
  print("you can give your choice")
else:
  print("you cant give your choice")