#Problem 1404
#Solved on 29.5.24

class Solution(object):
    def numSteps(self, s):
        steps = 0
        carry = 0
        n = len(s) - 1
        for i in range(n, 0, -1):
            if int(s[i]) + carry == 1:
                carry = 1
                steps += 2
            else:
                steps += 1
        return steps + carry
