#Problem 1190
#Solved on 11.7.24

from collections import deque 

class Solution:
    def reverseParentheses(self, s): 
        ind_stack = deque()
        res = []

        for char in s:
            if char == "(":
                ind_stack.append(len(res)) 
            elif char == ")": 
                start_ind = ind_stack.pop()
                res[start_ind:] = res[start_ind:][::-1]
            else:
                res.append(char)

        return "".join(res)
    

s = Solution()
print(s.reverseParentheses("a(bcdefghijkl(mno)p)q"))
