def no_of_one_bits(num):
    num = str(bin(num))
    count = 0
    for i in num:
        if i == '1':
            count += 1
    return count

num = 2147483645
ans = no_of_one_bits(num)
print(ans)