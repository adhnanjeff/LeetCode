#Problem 2881
import pandas as pd

class Solution(object):
    def selectData(self, employees):
        data = pd.DataFrame(employees, columns=["name","salary"]) 
        data['bonus'] = data['salary'] * 2
        return data

employees = [
    ["Piper", 4548],
    ["Grace", 28150],
    ["Georgia", 1103],
    ["Willow", 6593],
    ["Finn", 74576],
    ["Thomas", 24433]
]

s = Solution()
ans = s.selectData(employees)
print(ans)