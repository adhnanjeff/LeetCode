#Problem 260
#Solved on 31.5.24

def singleNumber(nums):
    freq_dict = {}
    for num in nums:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
        
    uni_num = [num for num, fre in freq_dict.items() if fre == 1]
    return uni_num

print(singleNumber([1, 2, 1, 3, 2, 5]))