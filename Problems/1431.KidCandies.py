#Problem 1431

def findKid(num, k):
    maxCandy = max(num)
    res = []
    for i in range(len(num)):
        if num[i] + k >= maxCandy:
            res.append(True)
        else:
            res.append(False)
    return res


candies = [12,1,12]
extra_candies = 10
ans = findKid(candies, extra_candies)
print(ans)