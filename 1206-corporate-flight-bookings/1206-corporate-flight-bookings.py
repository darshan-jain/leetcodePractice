class Solution:
    def corpFlightBookings(self, bookings: list[list[int]], n: int) -> list[int]:
        res = [0]* n 
        for f,l,s in bookings:
            res[f-1]+=s
            if l <n:
                res[l] +=-s
        return list(accumulate(res))
        