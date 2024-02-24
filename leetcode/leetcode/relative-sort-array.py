class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dic1={}
        dic2 ={}
        for i in arr1:
            if i in arr2:
                if i in dic1:
                    dic1[i]+=1
                else:
                    dic1[i]=1
            else:
                if i in dic2:
                    dic2[i] +=1
                else:
                    dic2[i] = 1
        output =[]
        for i in arr2:
            value = dic1[i]
            while value:
                output.append(i)
                value -=1
        for key,value in sorted(dic2.items()):
            while value:
                output.append(key)
                value-=1
        return output

 