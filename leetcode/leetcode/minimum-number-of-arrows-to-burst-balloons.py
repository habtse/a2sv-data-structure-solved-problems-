class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        print(points)
        count =1
        start = points[0][0]
        end = points[0][1]

        for i in range(len(points)):
            curr_start , curr_end = points[i]
            if curr_start > end:
                count +=1
                start = curr_start
                end = curr_end
            if curr_end < end:
                end = curr_end
        return count