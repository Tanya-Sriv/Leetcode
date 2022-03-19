class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxm = 0
        current = 0
        for i in nums: 
            if i == 1:
                current+=1                    
            else:
                if current > maxm:
                    mamx = current                   
                if maxm >= len(nums)/2:
                    return maxm
                current = 0
            maxm = max(maxm, current)
        return maxm