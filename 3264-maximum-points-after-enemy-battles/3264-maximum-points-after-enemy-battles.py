class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        enemyEnergies.sort()

        points = 0 
        j = len(enemyEnergies)-1
        while j>=0:
            if currentEnergy <enemyEnergies[0]:
                return points
            points+=(currentEnergy//enemyEnergies[0])
            currentEnergy = currentEnergy%enemyEnergies[0]

            currentEnergy+=enemyEnergies[j]
            j-=1
        return points
        