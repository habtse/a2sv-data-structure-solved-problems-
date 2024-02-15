class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ls =[]
        count =0
        for i in s:
            if i =='(':
                ls.append(i)
            elif i ==')':
                if len(ls) !=0:
                    last = ls.pop()
                else:
                    count +=1
        print(len(ls))  
        count +=len(ls)
        return count
