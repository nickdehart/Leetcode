class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        digits = [i for i in str(x)]
        for i, digit in enumerate(digits):
            if digit != digits[len(digits) - 1 - i]:
                return False
        return True
