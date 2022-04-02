class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        if max(nums) < l:
            return l
        return l*(l+1)//2 - sum(nums)
        