import math


def square(number):
   return (number ** 2) 

result = square(4)
print(result)

# a function with multiple params
def add(num1, num2):
   return num1 + num2

print(add(4,5))

# Polymorphism write a function multiply that multiplies two numbers, but can also accept and multiply strings.
def multiply(p1, p2):
   return p1 * p2

print(multiply(8, 10))
print(multiply('b', 11))
print(multiply(11, 'b'))

# Create a func that returns both area and circumference of a circle given its radius.
def circle_stats(radius):
   area =  math.pi * radius ** 2
   circumference = 2 * math.pi * radius
   return area, circumference
a,c = circle_stats(3)
print("Area: ",a, " Circumference: ", c)

# greet with default value
def greet (name = "User"):
   return "Hello, " + name + " !"
print (greet("Mayank"))

# Lambda function to calculate the cube of a number
cube = lambda x: x**3
print(cube(3))

# Function with *args
def sumAll(*args):
   print(args)
   return sum(args)
print(sumAll(1,2))
print(sumAll(1,2, 2,5,3,5,3))
print(sumAll(1,2, 2,5,3,5,3,67,5,63,3,2,463,2345))

# Function with **kwargs
def myDef(name, power):
   print("Name : ", name," Powers : ", power)
myDef(power = "Flying", name ="Superman")

def print_kwargs(**kwargs):
   for key, value in kwargs.items():
      print(f"{key}:{value}")

print_kwargs(power = "Flying", name ="Superman")
print_kwargs(name ="Superman")
print_kwargs(name ="Superman", power = "Flying", enemy = "Batman")

# Generator function that yields even numbers upto a specific limit
def even_generator1(limit): # normal function
    li = []
    for i in range(2, limit + 1, 2):
      li.append(i)
    return li
print(even_generator1(10))

def even_generator2(limit): # normal function
    for i in range(2, limit + 1, 2):
        yield i
for num in even_generator2(10):
    print(num)

# Recursive function to calculate the factoria; of a number
def factorial(n):
   if n == 0:
    return 1
   else:
    return n * factorial(n-1)
print(factorial(5))