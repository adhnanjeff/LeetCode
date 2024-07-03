#Problem 350
#Solved on 2.7.24

class Solution:
    def intersect(self, nums1, nums2):
        freq=[0]*1001
        for x in nums1:
            freq[x]+=1
        ans=[]
        for x in nums2:
            if  freq[x]>0:
                ans.append(x)
                freq[x]-=1
        return ans
        
s = Solution()
print(s.intersect([1,2,2,1],[2,2]))