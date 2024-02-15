class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count_5 = 0
        count_10 =0
        for i in range(len(bills)):
            
            if bills[i]==5:
                count_5 +=1
            elif bills[i] == 10:
                count_10 +=1
                count_5 -=1
            else:
                if count_10==0 :
                    count_5 -=3
                else:
                    count_10 -=1
                    count_5 -=1
            if count_5 <0:
                return False
        return True
