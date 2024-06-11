#Problem 1122
#Solved on 11.6.24

class Solution:
    def relativeSortArray(self, arr1, arr2):
        sorted_lst = []

        for x in arr2:
            while x in arr1:
                sorted_lst.append(x)
                arr1.remove(x)

        return(sorted_lst+sorted(arr1))
    
s = Solution()
arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
ans = s.relativeSortArray(arr1, arr2)
print(ans)