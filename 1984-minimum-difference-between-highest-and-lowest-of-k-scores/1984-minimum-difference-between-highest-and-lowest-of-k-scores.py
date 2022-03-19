class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        m = float('inf') 
        l,r = 0,k-1
        while r < len(nums):
            m = min(m,nums[r]-nums[l])
            r+=1
            l+=1
        return m
            
            