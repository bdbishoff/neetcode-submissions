class Solution:
    def isPalindrome(self, s: str) -> bool:
        f = ""
        for c in s:
            if c.isalnum():
                f += c.lower()
        return f == f[::-1]
        