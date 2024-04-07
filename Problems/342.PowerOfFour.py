#Problem 342

def powerOfFour(n):

    if n <= 0:
        return False
    
    while n % 4 == 0:
        n //= 4

    return n == 1

n = 16
ans = powerOfFour(n)
print(n)