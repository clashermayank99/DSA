# Factors of a given number

n = 36

# Brute force , TC = O(N), SC = O(K) where K is total number of factors
class Solution1:
    def returnAllFactors(self, x:int)->list[int]: 
        num = x
        result = []
        for i in range (1, num+1):
            if num % i == 0:
                result.append(i)
        return result

allFactors = Solution1()
print(allFactors.returnAllFactors(n))

# Better solution , TC == O(N/2), SC = O(K)
class Solution2:
    def returnAllFactors(self, x:int)->list[int]:
        num = x
        result = []
        for i in range (1, (num//2)+1):
            if num % i == 0:
                result.append(i)
        result.append(num)
        return result
allFactors2 = Solution2()
print(allFactors2.returnAllFactors(n))

# Optimal solution, TC= O(sqrt(N)) + O(N log N), SC = O(K)
from math import sqrt
class Solution3:
    def returnAllFactors(self, x:int)->list[int]:
        result = []
        num= x
        for i in range(1, int(sqrt(num))+1):
            if num%i == 0:
                result.append(i)
                if num//i != i:
                    result.append(num//i)
        result.sort()
        return result

allFactors3 = Solution3()
print(allFactors3.returnAllFactors(n))

# LC question - 2427
from math import sqrt
class Solution4:
    def commonFactors(self, a: int, b: int) -> int:
        factors_of_a = []
        factors_of_b = []
        for i in range (1, int(sqrt(a))+1):
            if a % i == 0:
                factors_of_a.append(i)
                if a//i != i:
                    factors_of_a.append(a//i)
        for i in range (1, int(sqrt(b))+1):
            if b % i == 0:
                factors_of_b.append(i)
                if b//i != i:
                    factors_of_b.append(b//i)
        print("a :",factors_of_a)
        print("b :",factors_of_b)
        def getCommonValues(arr1: list[int], arr2: list[int]) -> list[int]:
            return list(set(arr1) & set(arr2))
        commonFactors = getCommonValues(factors_of_a, factors_of_b)
        return len(commonFactors)
commonFactors = Solution4()

print(commonFactors.commonFactors(12, 6))