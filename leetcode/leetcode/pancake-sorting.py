class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
             
        result = []
        if sorted(arr) ==arr:
            return result
        else:
            target = sorted(arr)
            for i in range(len(arr)-1,-1,-1):
                pivot = arr.index(target[i])
                if pivot != i:
                    result.append(pivot + 1)
                    arr = arr[pivot::-1] + arr[pivot +1:]
                    result.append(i + 1)
                    arr = arr[i::-1] + arr[i+1:]
            return result
                