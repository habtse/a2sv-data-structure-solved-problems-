class TimeMap:

    def __init__(self):
        self.dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dic:
            self.dic[key].append([timestamp,value])
        else:
            self.dic[key] = [[timestamp,value]]
        
    def get(self, key: str, timestamp: int) -> str:
        if  key not in self.dic:
            return ""
        if timestamp < self.dic[key][0][0] :
            return ""
        if timestamp >= self.dic[key][-1][0]:
            return self.dic[key][-1][1]
            
        low, high = 0,len(self.dic[key]) -1
        while low < high:
            
            mid = low + ((high - low) // 2)
            
            if self.dic[key][mid][0] <= timestamp:
                low = mid + 1
            else :
                high = mid
        return self.dic[key][low-1][1]
    
        
        

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)