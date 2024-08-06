#Problem 3016
#Solved on 6.8.24

class Solution:
    def minimumPushes(self, word: str) -> int:
        frequency_map = Counter(word)
        max_heap = [(-freq, char) for char, freq in frequency_map.items()]
        heapq.heapify(max_heap)

        count = 0
        j = 1
        
        while max_heap:
            freq, char = heapq.heappop(max_heap)
            freq = -freq  
            if j <= 8:
                count += freq
            elif j <= 16:
                count += freq * 2
            elif j <= 24:
                count += freq * 3
            else:
                count += freq * 4
            j += 1
        return count