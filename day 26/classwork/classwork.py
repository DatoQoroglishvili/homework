def print_range(start, end):
    for i in range(start, end + 1):
        print(i, end)

print_range(10, 15)
#2
def u_range(start, end):
    total = 0
    for i in range(start, end + 1):
        total += i
    return total

result = u_range(2, 7)
print(result)
#3
def calculate_arithmetic(start, end):
    numbers = []

    for i in range(start, end):
        numbers.append(i)
    
    result = sum(numbers) / len(numbers)

    print(result)

calculate_arithmetic(5, 11)
#4
def calculate_arithmetic(start, end):
    numbers = []

    for i in range(start, end):
        numbers.append(i)
    
    result = sum(numbers) / len(numbers)

    print(result)

calculate_arithmetic(5, 11)
#5
def create_variable():
    variable = "created outside  function"
    return variable

var = create_variable()
print(var) 
#6








#7
def calculate_sums(numbers_list):
    total = sum(numbers_list)
    return total
numbers = [1, 2, 3, 4, 5]
results = calculate_sums(numbers)
print(results)
#8
def even_indexed_letters(name):
    new_string = ""
    for i, letter in (name):
        if i % 2 == 0:
            new_string += letter
    return new_string

name = input("Enter a name:")
result = even_indexed_letters(name)
print(name,result)