class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort()
        print(tasks)
        maxx = processorTime[0]+tasks[-1]
        for i in range(1,len(processorTime)):
            maxx = max(processorTime[i]+tasks[ i*-5+i-1], maxx)
        return maxx

