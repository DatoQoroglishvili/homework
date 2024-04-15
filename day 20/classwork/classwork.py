#1
list1= ([5, 8, 12, 18, 22])
print(list1[0] + list1[1])

list2= ([7, 15, 12, 18, 22])
print(list2[0] + list2[2])

list3= ([25, 42, 12, 18, 22])
print(list3[2] + list3[3])

#2
numbers = [1,2,3,4]
even_numbers = []
for i in numbers:
    if i % 2 == 0:
        even_numbers.append(i)
print(even_numbers)
#3
a = ["b", "c", "b", "a"]
b = ["",  "a", "a", "c"]

score = 0

for index in range(len(a)):
    if a[index] == b[index]:
        score = score + 4
    elif a[index] == "" or b[index] == "":
        score = score + 0
    else:
        score = score - 1

print(score)