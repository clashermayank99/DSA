# Reverse a number LC - 7
n = 1234

class Solution:
    def reverse(self, x: int) -> int:
        num = abs(x) #abs basically gives non negative numbers
        result = 0
        while num >0:
            last_digit = num%10
            result = (result*10)+last_digit
            num = num//10
        if x > 0 and result < 2**31:
            return result
        elif x <0 and result <= 2**31:
            return -result
        else:
            return 0
reversed = Solution()
print(reversed.reverse(n))