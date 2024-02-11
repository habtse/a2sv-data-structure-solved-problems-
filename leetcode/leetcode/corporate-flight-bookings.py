class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ls = [0]*(n+1)
        for first,last,seat in bookings:
            ls[first-1] +=seat
            ls[last]  -=seat
        total = 0
        prefix = []
        for i in range(len(ls)-1):
            total +=ls[i]
            prefix.append(total)
        return prefix

