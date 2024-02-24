class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        right = points[1][0]
        left = points[0][0]
        maxx = right-left
        for i in range(2,len(points)):
            left = right
            right = points[i][0]
            maxx = max(maxx,right-left)
        return maxx