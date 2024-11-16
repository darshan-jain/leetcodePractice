class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        sum = 1
        i=1
        n = len(ratings)
        while i < n :
            if ratings[i] == ratings[i-1]:
                sum = sum+1
                i +=1
                continue
            peak = 1
            while i< n and ratings[i] > ratings[i-1]:
                peak +=1
                sum+=peak
                i+=1
            down = 1
            while i<n and ratings[i] < ratings[i-1]:
                sum +=down
                i+=1
                down+=1
            if down > peak:
                sum += down-peak

        
        return sum