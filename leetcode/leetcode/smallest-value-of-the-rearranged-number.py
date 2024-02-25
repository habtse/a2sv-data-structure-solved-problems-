class Solution:
    def smallestNumber(self, num: int) -> int:
        
        # print(ls)
        if num > 9:
            ls = sorted(str(num))
            index =0
            while  ls[index] =='0':
                index +=1
            ls[index] , ls[0] = ls[0],ls[index]
            return int(''.join(ls))
        elif num <0:
            ls = sorted(str(num), reverse = True)
            return -int(''.join(ls[:-1]))

            
        return num