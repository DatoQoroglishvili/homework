#1
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
#2
num = int(input("enter number"))
if num > 0 :
    print("this number is possitive")
elif num < 0 :
    print("this number is negative")
else :
    print("this number is zero")
#3
for i in range(2, 101, 2):
    print(i)
#4
total = 0
number = 1
while number <= 100:
    total += number
    number += 1

print("ყველა რიცხვის ჯამი 1-დან 100-მდე არის:", total)
#5
day_number = int(input("enter week day 1 to 7"))
if day_number == 1:
    print("monday")
elif day_number == 2:
    print("tuesday")
elif day_number == 3:
    print("wednesday")
elif day_number == 4:
    print("thuresday")
elif day_number == 5:
    print("friday")
elif day_number == 6:
    print("saturday")
elif day_number == 7:
    print("sunday")
else:
    print("its incorrect number")
#7
number = int(input("enter number "))
if number == 0:
    print("its zero")
elif number % 2 == 0:
    print("its even")
else:
    print("its oven")