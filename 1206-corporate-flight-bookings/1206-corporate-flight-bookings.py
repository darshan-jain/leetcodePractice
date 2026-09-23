# #prefix sum 
# [[1,2,10],[2,3,20],[2,5,25]]

# Flight labels:        1   2   3   4   5
# Booking 1 reserved:  10  10
# Booking 2 reserved:      20  20
# Booking 3 reserved:      25           25
# Total seats:         10  55  45  25  25

# #need to keep track of open and close intervals 

# open = {
#     1:10,
#     2:20,25
    
# }

# close = {
#     2:10,
#     3:20,
#     5:25
# }

# currval = 10 at 1
# 1 - currval + open at 1 - close at 0 
# 2 - currval+ open at 2 (20,25) - close at 1 = 55
# 3 - currval + open at 3 - close at 2 = 55 - 10 = 45


class Solution:
    def corpFlightBookings(self, bookings: list[list[int]], n: int) -> list[int]:
        opens = defaultdict(int)
        close = defaultdict(int)
        for book in bookings:
            s = book[0]
            e = book[1]
            seat = book[2]
            opens[s]+= seat
            close[e]+=seat
        
        res = [0]*(n+1)
        currval = 0 
        for i in range(1,n+1):
            if opens[i]:
                currval+=opens[i]
            if close[i-1]:
                currval-=close[i-1]
            res[i] = currval

        return res[1:]