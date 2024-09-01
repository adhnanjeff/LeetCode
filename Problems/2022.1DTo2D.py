#Problem 2022
#Solved on 1.9.24

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        matrix=[]
        if (m*n)!=len(original):
            return matrix
        k=0
        for i in range(0,len(original),n):
            matrix.append(original[i:i+n])
            k=k+n
        return matrix

        