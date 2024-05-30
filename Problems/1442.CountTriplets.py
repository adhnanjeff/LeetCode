#Problem 1442
#Solved on 30.5.24

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        res, hashmap, cur = 0, defaultdict(list), 0
        for i, ele in enumerate(arr):
            cur ^= ele
            if cur == 0:
                res += i
            if cur in hashmap:
                for after in hashmap[cur]:
                    res += (i - after - 1)
            hashmap[cur] += [i]
        return res