#Problem 412

class Solution(object):
    def fizzBuzz(self, n):
        array = []
        for i in range (1, n+1):
            if i % 15 == 0:
                array.append("FizzBuzz")
            elif i % 3 == 0:
                array.append("Fizz")
            elif i % 5 == 0:
                array.append("Buzz")
            else:
                array.append(str(i))
        return array
        
sol = Solution()
ans = sol.fizzBuzz(15)
print(ans)