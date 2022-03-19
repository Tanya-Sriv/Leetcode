class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = nums[0]
        c_sum = 0
        for i in nums:
            if c_sum < 0 :
                c_sum = 0
            c_sum += i
            m = max(m, c_sum)
        return m
            
        