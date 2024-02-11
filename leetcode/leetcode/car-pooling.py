class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        ls = [0]*1002
        for numsPassengers,begin,end in trips:
            ls[begin] += numsPassengers
            ls[end ] -=numsPassengers
        
        total =0
        for i in ls:
            total +=i
            if total >capacity:
                return False
        return True
        