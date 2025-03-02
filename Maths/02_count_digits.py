# Count the number of digits
count = 0
n = 5873
num = n
while num >0:
    count += 1
    num = num//10

print(count)

# Another optimal approach using log of base 10
from math import *

def countDigits(num):
    return int(log10(num)+1)

# Similar question Solved on GFG too.