# Check Palindrome, LC - 9

n = 1234321
class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = x
        result = 0
        while num>0:
            last_digit = num%10
            result = (result*10)+last_digit
            num = num//10
        return x ==  result

isPalindrome = Solution()
print(isPalindrome.isPalindrome(n))