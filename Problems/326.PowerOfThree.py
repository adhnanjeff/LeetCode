#Problem 326

def powerOfThree(n):

    if n <= 0:
        return False
    
    while n % 3 == 0:
        n //= 3

    return n == 1

n = 27
ans = powerOfThree(n)
print(n)