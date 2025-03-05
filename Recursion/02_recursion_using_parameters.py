# Recursion using Parameters
# Print x n-times with recursion
def func1(x,n): #Head recursion
    if n == 0:
        return
    print(f'Head Recursion {n} : {x}')
    func1(x,n-1)

func1(15, 4)

def func2(x,n): #Tail recursion
    if n == 0:
        return
    func2(x,n-1)
    print(f'Tail Recursion {n} : {x}')

func2(15, 4)

# Print 1 to n using recursion
def func3(i, n): #Head Recursion
    if i>n:
        return
    print(f'Head Recursion {i}')
    func3(i+1,n)
func3(1,4)

def func4(n): #Tail recursion
    if n==0:
        return
    func4(n-1)
    print(f'Tail Recursion {n}')
func4(4)

# Print n to 1 using Recursion
def func5(n): #Head Recursion
    if n == 0:
        return
    print("Head",n)
    func5(n-1)
func5(4)

def func6(i,n): #Tail Recursion
    if i>n:
        return
    func6(i+1,n)
    print("Tail",i)
func6(1,4)