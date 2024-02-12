#Lists are used to store multiple items in a single variable.
#example
thislist = ["apple", "banana", "cherry"]
print(thislist)

my_list1=("banana,apple,hotdog")
print(my_list1)
#checking class type:
print(type("my_list1"))

#removing iteams from our list
my_List49=("saba","nika","banana","luka")
print(my_List49)
#we need to use () to remove iteam
my_List49.remove("banana") #we need to use () to remove iteam

#To add an item to the end of the list, use the append() method:
#Using the append() method to append an item:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)


#Add elements of a tuple to a list:
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#List items are indexed and you can access them by referring to the index number:
#Print the second item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[1]) #it will print ("banana")

thislist = ["apple", "banana", "cherry"]
print(thislist[2]) #it will print("cherry")

#You can specify a range of indexes by specifying where to start and where to end the range.
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) #it will print("Cherry","orange","kiwi")from list.


#Change Item Value
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant" # here "blackcurrant" will replace banana with himself in the list
print(thislist) # we will have new list with blackcurrant in it

#Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"] 
print(thislist)

#Sort List Alphanumerically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
#Sort the list numerically:
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#Sort Descending]
#To sort descending, use the keyword argument reverse = True:

#Sort the list descending:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist) # it will print Alphanumerically but reverse for example['pineapple', 'orange', 'mango', 'kiwi', 'banana']

#Join Two Lists
#One of the easiest ways are by using the + operator or  the extend() method
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3) 
# we combined list1 and list2 and got list3
