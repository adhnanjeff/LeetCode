#Problem 2880
import pandas as pd

class Solution(object):
    def selectData(self, students):
        data = pd.DataFrame(students, columns=["student_id","name","age"]) 
        return data[data.student_id == 101].get(['name', 'age'])
    

students = [
    [101, "Ulysses", 13],
    [53, "William", 10],
    [128, "Henry", 6],
    [3, "Ulysses", 11]
]

s = Solution()
ans = s.selectData(students)
print(ans)
