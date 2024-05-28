#Problem 29


class Solution(object):
    def divide(self, dividend, divisor):
        if dividend == 0:
            return 0
        
        sign = -1 if (dividend < 0) != (divisor < 0) else 1
        
        a, b = abs(dividend), abs(divisor)
        
        res = 0
        while a >= b:
            temp, multiple = b, 1
            while a >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            a -= temp
            res += multiple
        
        res *= sign
        
        return min(max(-2147483648, res), 2147483647)
