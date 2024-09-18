#Problem 884
#Solved on 17.9.24

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s_words = s1.split()
        t_words = s2.split()
        diff = list(set(s_words) - set(t_words)) + list(set(t_words) - set(s_words))
        return [word for word in diff if s_words.count(word) == 1 or t_words.count(word) ==1]

        