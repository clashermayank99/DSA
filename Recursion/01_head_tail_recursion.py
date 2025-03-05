# Head Recursion:

count1 = 0
def func1():
    global count1
    if count1 == 4:
        return
    print("Hey",count1)
    count1 += 1
    func1()
func1()

# Tail Recursion: It is also called Backtracking
count2 = 0
def func2():
    global count2
    if count2 == 4:
        return
    count2 += 1
    func2()
    print("Hello",count2)
func2()