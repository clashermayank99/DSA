numbers = [1, 10, -3, 5, -4, -6, 6, 7, -7, 10, -10, 11, -15, 19]
finalNumberCount = 0
for i in numbers:
    if i >=0:
        finalNumberCount += 1
        print(i)
print("finalNumberCount", finalNumberCount)

n = 10
sum_even = 0

for i in range(1, n+1):  #from 1 to n i.e. 10
    if i % 2 ==0:
        sum_even+= i
print(sum_even)

# Reverse the string using loop
input_str = "Welcome"
reversed_str = ""

for char in input_str:
    reversed_str = char + reversed_str
print(reversed_str)

# Find the first non repeated character
input_str = "teeteracdacd"

for char in input_str:
    if input_str.count(char) ==  1:
        print("first non repeated character: ", char)
        break

# Compute the factorial of a number using a while loop
number = 5
factorial = 1

while number >0:
    factorial *= number
    number -=1
print("factorial :",factorial)

# Users input until input is between 1 to 10
# while True:
#     number = int(input("Enter the value b/w 1 and 10 :"))
#     if 1<= number <=10:
#         break

# find prime number
number = 28
is_prime = True
if number >1:
    for i in range(2, number):
        if (number % i) == 0:
            is_prime = False
            break
print(is_prime)

# Check if all in a list are unique if duplicate exit the loop and print duplicate
items = ["apple","banana", "orange","apple","mango"]
unique_item = set()
for item in items:
    if item in unique_item:
        print("Duplicate item :", item)
        break
    unique_item.add(item)
    