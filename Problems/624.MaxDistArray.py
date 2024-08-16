#Problem 624
#Solved on 16.8.24

#170-ms
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        if len(arrays) < 2:
            return 0
        
        global_min, global_max = arrays[0][0], arrays[0][-1]
        result = 0

        for arr in arrays[1:]:
            local_min, local_max = arr[0], arr[-1]
            result = max(result, max(local_max - global_min, global_max - local_min))
            global_min = min(global_min, local_min)
            global_max = max(global_max, local_max)

        return result

def main():
    input = sys.stdin.read().strip()
    

    test_cases = input.splitlines()
    
    results = []
    for case in test_cases:
       
        arrays = json.loads(case)
        results.append(Solution().maxDistance(arrays))
    

    with open('user.out', 'w') as f:
        for result in results:
            f.write(f"{result}\n")

if __name__ == "__main__":
    main()
    exit(0)


