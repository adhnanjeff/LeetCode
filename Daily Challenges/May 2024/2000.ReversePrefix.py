#Problem 2000
#Solved on 1.5.24

class Solution(object):
    def reversePrefix(self, word, ch):
        j = word.find(ch)
        if j != -1:
            return word[:j+1][::-1] + word[j+1:]
        return word
    
s = Solution()
word = "abcdefd"
ch = "d"
ans = s.reversePrefix(word, ch)
print(ans)