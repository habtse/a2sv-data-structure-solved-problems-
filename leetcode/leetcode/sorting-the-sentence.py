class Solution:
    def sortSentence(self, s: str) -> str:
        ls = s.split()
        ls.sort(key= lambda x : x[-1])
        for i in range(len(ls)):
            ls[i] = ls[i][:len(ls[i])-1]
        return ' '.join(ls)
            