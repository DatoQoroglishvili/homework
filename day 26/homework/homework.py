#1
def sum(nums):
    totaly = 0
    for i in range(len(nums)):
        if i % 2 == 0:
            totaly += nums[i]
    return totaly
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum(nums)
print("Sum of nums at even indices:", result)

#2
def even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(even(2))
print(even(3))
#
def prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
print(prime(7))
print(prime(10))
#4
def name(names):
    name = [name() for name in names]
    return name
name = ["david", "chad", "gigachad"]
print(name(name))

#5
def nums(numbers):
    update_nums = []
    for num in numbers:
        if num % 2 == 0:
            update_nums.append(num * 2)
        else:
            update_nums.append(num // 2)
    return update_nums
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums(nums))