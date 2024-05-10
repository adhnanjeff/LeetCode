#Problem 786
#Solved on 10.5.24

class Solution:
    def kthSmallestPrimeFraction(self, a: List[int], k: int) -> List[int]:
        return nsmallest(k,combinations(a,2),lambda q:q[0]/q[1])[-1]