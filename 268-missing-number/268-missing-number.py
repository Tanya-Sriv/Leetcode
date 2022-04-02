class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        m = max(nums)
        l = len(nums)
        if m < l:
            return len(nums)
        return l*(l+1)//2 - sum(nums)
        