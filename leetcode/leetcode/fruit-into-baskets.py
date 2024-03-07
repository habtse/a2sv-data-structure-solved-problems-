class Solution:
    def totalFruit(self, fruits: List[int]) -> int:        
        buckets = deque([{fruits[0]:1}])
        # types = deque[fruits[0]]
        
        result = float('-inf')
        for i in range(1,len(fruits)):
            
            if fruits[i]  in buckets[0]:
                
                buckets[0][fruits[i]] += 1

                poped = buckets.popleft()
                print (poped)
                buckets.append(poped)
            elif len(buckets) ==1:
                buckets.append({fruits[i]: 1})
            
            elif fruits[i]  in buckets[1]:
                buckets[1][fruits[i]] += 1
            else:
                # result = max(result,list(buckets[1].values())[0] + list(buckets[0].values())[0] )
                # types.append(fruits[i])
                last = 0
                count =0
                for j in range(i-1,-1,-1):
                    if fruits[j] ==list(buckets[0].keys())[0]:
                        last = j +1
                        print('here1')
                    if last and fruits[j] ==list(buckets[1].keys())[0]:
                        print ('here')
                        count += 1
                    if not (fruits[j] ==list(buckets[1].keys())[0] or fruits[j] ==list(buckets[0].keys())[0]):

                        break
                # value = fruits[fruits.index(list(buckets[1].keys())[0]):last].count(list(buckets[1].keys())[0])
                buckets[1][list(buckets[1].keys())[0]] -= count
                buckets.popleft()
                buckets.append({fruits[i]: 1})
            if len(buckets) ==2:
                result = max(result,list(buckets[1].values())[0] + list(buckets[0].values())[0] )
        if len(buckets)==1:
            result = max(result,list(buckets[0].values())[0] )
        
        
        return result

            