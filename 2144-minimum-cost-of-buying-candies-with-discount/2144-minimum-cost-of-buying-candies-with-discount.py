class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost = sorted(cost, reverse=True)
        for i in range(2, len(cost),3):
            cost[i]=0
        return sum(cost)
            