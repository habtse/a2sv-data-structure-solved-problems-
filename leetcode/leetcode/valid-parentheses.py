class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'{':'}','[':']','(':')'}
        ls = []
        for i in s:
            if i in dic:
                ls.append(i)
            else:
                if len(ls)>0:
                    endValue = ls.pop()

                    if i != dic[endValue]:
                        return False
                else:
                    return False
        if len(ls) >0:
            return False
        return True
                