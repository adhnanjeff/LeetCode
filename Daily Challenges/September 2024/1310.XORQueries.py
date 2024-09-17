#Problem 1310
#Solved on 13.9.24

class Solution(object):
    def xorQueries(self, arr, queries):
        prefix_xor = []
        res = []
        xor = 0

        for num in arr:
            xor = xor ^ num
            prefix_xor.append(xor)

        for q in queries:
            if q[0] == 0:
                val = prefix_xor[q[1]]
            else:
                val = prefix_xor[q[1]] ^ prefix_xor[q[0] - 1]
            res.append(val)

        return res
        