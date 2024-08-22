#Problem 476
#Solved on 22.8.24

class Solution:
    def findComplement(self, a: int) -> int:
        b = 1

        while a >= b:
            a ^= b
            b <<= 1
        
        return a