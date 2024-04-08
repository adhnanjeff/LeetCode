#Problem 1700

def studentsUnableToEat(students, sandwiches):
    n = len(students)
    i = 0

    while i < n:
        if students[0] == sandwiches[0]:
            students.pop(0)
            sandwiches.pop(0)
            n -= 1  # Update the number of students
            i = 0  # Reset the index to check from the beginning
        else:
            students.append(students.pop(0))
            i += 1  # Move to the next student

    return len(students)

students = [1,1,1,0,0,1]
sandwiches = [1,0,0,0,1,1]

ans = studentsUnableToEat(students, sandwiches)
print(ans)

