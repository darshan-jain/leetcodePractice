class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if bills[0] != 5:
            return False
        
        count5 = 0
        count10 = 0
        count20 = 0 

        for bill in bills:
            if bill == 5:
                count5+=1
            if bill == 10:
                if count5 >=1:
                    count10+=1
                    count5-=1
                else:
                    return False
            if bill == 20:
                if (count10 >= 1 and count5 >=1) or count5 >=3:
                    if count10 >= 1 and count5 >=1:
                        count20+=1
                        count10-=1
                        count5-=1
                    elif count5 >= 3:
                        count20+=1
                        count5-=3
                else:
                    return False
        
        return True
        