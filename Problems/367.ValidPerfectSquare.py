#Problem 367

def isPerfectSquare(num):
    if num < 0:
        return False
    if num == 0:
        return True

    left, right = 1, num
    while left <= right:
        mid = left + (right - left) // 2
        square = mid * mid
        if square == num:
            return True
        elif square < num:
            left = mid + 1
        else:
            right = mid - 1

    return False

num = 2000105819
ans = isPerfectSquare(num)
print(ans)
