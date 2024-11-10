class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five = 0 
        ten =0 
        twenty =0 
        for bill in bills:
            if bill == 5:
                five +=1
            if bill == 10:
                if five >0:
                    ten+=1
                    five-=1
                else:
                    return False
            if bill == 20:
                if ten >0 and five>0:
                    ten-=1
                    five-=1
                    twenty+=1
                elif five>2:
                    five-=3
                    twenty+=1
                else:
                    return False
        return True

        