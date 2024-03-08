#1
for i in range(0, 21):
    print(i)
#2
num1 =int(input("please enter first number: "))
num2 =int(input("please enter second number: "))
if  num1 > num2:   
    for i in range(num2, num1):
        print(i)
elif num2>num1:
    for i in range(num1, num2):
        print(i)
else: 
    print(f"{num1}={num2}")
#3
for i in range(50, 101):
    print(i)
#4
for i in range(100, 49, -1):
    print(i)   

#5
sum=0
for i in range(0, 51):
    sum=sum+i
print(sum)

#6
num3 =int(input("please enter positive number: "))
for i in range(0, num3):
    print(i)

#7
user_age=int(input("Please enter your age: "))
new_user_age=user_age + 10
for i in range(user_age +1, new_user_age):
    print(i)