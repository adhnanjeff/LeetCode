#Problem 989

def addArray(num, k):
    st = ""
    for i in num:
        st += str(i)
    st = int(st) + k
    res = []
    res.append(st)
    split_array = [int(i) for i in str(res[0])] 
    return split_array

num = [1,2,0,0]
k = 34
ans = addArray(num, k)
print(ans)