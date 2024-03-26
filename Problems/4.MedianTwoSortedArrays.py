import math
def findMedianSortedArrays(nums1, nums2):
    size_1 = len(nums1)
    size_2 = len(nums2)

    res = []
    i, j = 0, 0
 
    while i < size_1 and j < size_2:
        if nums1[i] < nums2[j]:
            res.append(nums1[i])
            i += 1
        else:
            res.append(nums2[j])
            j += 1
    res = res + nums1[i:] + nums2[j:]

    if len(res) % 2 == 0:
        mid1 = len(res) // 2 - 1
        mid2 = mid1 + 1
        return (res[mid1] + res[mid2]) / 2
    mid = len(res) // 2 
    return res[mid]


nums1 = [1,2]
nums2 = [3,4]
ans = findMedianSortedArrays(nums1, nums2)
print(ans)