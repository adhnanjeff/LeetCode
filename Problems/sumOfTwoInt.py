#Problem 371

class Solution(object):
    def getSum(self, a, b):
        while b!=0:
            carry = a & b;
            a = a ^ b;
            b = carry << 1;
        return a
        