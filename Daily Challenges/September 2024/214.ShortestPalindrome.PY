#Problem 214
#Solved on 20.9.24

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        r = s[::-1]
        for i in range(len(s) + 1):
            if s.startswith(r[i:]):
                return r[:i] + s
