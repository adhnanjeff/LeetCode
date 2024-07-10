#Problem 1598
#Solved on 10.7.24

class Solution:
    def minOperations(self, logs):
        count=0
        for log in logs:
            if "./" not in log:
                count+=1
            elif "../" in log:
                count=max(0,count-1)
        return count
    
s = Solution()
logs = ["d1/","d2/","../","d21/","./"]
ans = s.minOperations(logs)
print(ans)