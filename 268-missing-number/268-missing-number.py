class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # l = len(nums)
        return len(nums)*(len(nums)+1)//2 - sum(nums)
        