#Problem 1137
#Solved on 24.4.2024

class Solution:
    def tribonacci(self, n):
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        
        T = [0, 1, 1]

        for i in range(3, n+1):
            T.append(T[i-1] + T[i-2] + T[i-3])


        return T[n]
    
s = Solution()
n = 10
ans = s.tribonacci(n)
print(ans)
