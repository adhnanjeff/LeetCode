#Problem 1482
#Solved on 19.6.24

class Solution(object):
    def minDays(self, bloomDay, m, k):
        if( m * k > len(bloomDay)):
            return -1
        l = min(bloomDay)
        h = max(bloomDay)
        
        while(l <= h):
            a = 0
            c = 0
            
            mid = (l + h) // 2
            for i in bloomDay:
                if i <= mid:
                    c += 1
                else:
                    a += c // k
                    c = 0
            a += c// k
            if a>=m:
                h=mid-1
            else:
                l=mid+1
        return l