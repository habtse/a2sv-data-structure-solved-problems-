class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        leng = len(s)
        ls = [0,0]
        dic = {}
        for i in range(leng):
            
            if s[i] in dic:
                values =dic[s[i]]
                values[1] = i
                dic[s[i]] = values
            else:
                values = [i,i]
                dic[s[i]] = values
        print (dic)
        output=[]
        begin,last =0,0
        for a,b in dic.values():
            if a ==0:
                begin , last = a,b
                continue
            if a < last :
                if b > last:
                    last = b
            else:
                output.append(last -begin +1)
                begin , last = a,b
        output.append(last -begin +1)
        return output

        