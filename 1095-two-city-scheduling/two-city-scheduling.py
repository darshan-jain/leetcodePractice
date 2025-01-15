class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        m = len(costs)
        
        n = m /2

        costs = sorted(costs, key = lambda x: abs(x[1]-x[0]), reverse = True)

        citya = 0
        cityb = 0 
        totalcost = 0 
        
        for item in costs:
            
            if item[0] < item[1] and citya<n:
                totalcost+=item[0]
                citya+=1
                
            elif item[0] > item[1] and cityb<n:
                totalcost+=item[1]
                cityb+=1
                
            
            else:
                if citya>=n:
                    totalcost+=item[1]
                    cityb+=1
                    
                else:
                    totalcost+=item[0]
                    citya+=1
                    
        
        # while citya<=n and ind <m:
        #     totalcost+=costs[ind][0]
        #     citya+=1
        
        # while cityb<=n and ind < m:
        #     totalcost+=costs[ind][1]
        #     cityb+=1

        
        
        
        return totalcost


        