# Ques : Sum of 1 to N
# Parameterized Recursion

def func1(sum, i, n):
    if i >n:
        print(sum)
        return
    func1(sum+i, i+1, n)
func1(0,1,4)

# Functional Recursion
def func2(n):
    if n == 1:
        return 1
    return n + func2(n-1)
result = func2(4)
print("func2",result)