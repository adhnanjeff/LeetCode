#Problem 1662

def checkEquivalence(a1, a2):
    
    return "".join(a1) == "".join(a2)
    """
    s1 = ""
    s2 = ""
    for char in a1:
        s1 += char
    for char in a2:
        s2 += char
    if s1 == s2:
        return True
    else:
        return False
    """

a1 = ["abc", "d", "defg"]
a2 = ["abcddefg"]
ans = checkEquivalence(a1, a2)
print(ans)