class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones)== 1:
            return stones[0]
        elif len(stones)> 1:
            stones = sorted(stones, reverse=True)
            while len(stones) > 2:
                m = stones.pop(0)
                n = stones.pop(0)
                stones.append(m - n)
                if m>n:
                    n = 0                    
                else:
                    m = 0
                stones = sorted(stones, reverse=True)
            if stones:
                return stones[0] - stones[1]               
        return 0
        # if len(stones)== 1:
        #     return stones[0]
        # elif stones == []:
        #     return 0
        # else:
        #     stones = sorted(stones, reverse=True)
        #     while len(stones) > 2:
        #         m = stones.pop(0)
        #         n = stones.pop(0)
        #         if m>n:
        #             k = m - n
        #             n = 0                    
        #         else:
        #             k = n-m
        #             m = 0
        #         stones.append(k)
        #         stones = sorted(stones, reverse=True)
        #     if stones:
        #         return stones[0] - stones[1]
        #     else:
        #         return 0
    
                
                    
        