# Armstrong number, LC - 1134
n = 153

class Solution:
    def isArmstrong(self, x: int) -> bool:
        result = 0
        length = len(str(x))
        num = x
        while num>0:
            last_digit = num%10
            result = result + (last_digit**length)
            num = num//10
        if x == result:
            return True
        else:
            return False

armstrongCheck = Solution()
print(armstrongCheck.isArmstrong(n))