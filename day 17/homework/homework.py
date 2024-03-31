#1
names = ["gio", "luka", "leqso", "dato", "nika"]
print(names[0],names[1],names[2],names[3],names[4])
#2
names = ["gio", "luka", "leqso", "dato", "nika"]
for i in names:
    print(i)
#3
total = 0
product = 1

for number in range(1, 11):
    total += number
    product *= number

print(total)
print(product)
#4
total = 0

for number in range(2, 11, 2):
    print(number)
    total += number

print(total)
#5
total= 0
product = 1

for number in range(1, 11, 2):
    print(number)
    total += number
    product *= number

print( total)
print(product)
#6
word = "wigni"

for e in word:
    print(e)
#7
word = "pepela"

for i in range(0, len(word), 2):
    print(word[i])