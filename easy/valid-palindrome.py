class Solution:
    def isPalindrome(self, s: str) -> bool:
        val = ''.join(filter(str.isalnum, s.lower()))
        return val == val[::-1]
