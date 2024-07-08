#Problem 1823
#Solved on 8.7.24

class Solution:
    def findTheWinner(self, n, k):
        circle = [num for num in range(1, n + 1, 1)]
        cur_ind = 0

        while len(circle) != 1:
            next_to_remove = (cur_ind + k - 1) % len(circle)
            circle.pop(next_to_remove)
            cur_ind = next_to_remove

        return circle[0]
    
s = Solution()
print(s.findTheWinner(5, 2))