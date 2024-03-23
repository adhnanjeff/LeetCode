#Problem 231

def isPowerOfTwo(self, n):
    if n <= 0:
       return False
    else:
        return n & n-1 == 0

ans = isPowerOfTwo(3)
print(ans)