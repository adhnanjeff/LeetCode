#Problem 2037
#Solved on 13.6.24

class Solution(object):
    def minMovesToSeat(self, seats, students):
        seats.sort()
        students.sort()
        result = 0

        for i in range(len(seats)):
            result += abs(seats[i] - students[i])

        return result
        

s = Solution()
seats = [3, 1, 5]
students = [2, 7, 4]
ans = s.minMovesToSeat(seats, students)
print(ans)