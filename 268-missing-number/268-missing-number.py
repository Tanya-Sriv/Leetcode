class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        return (l*l+l)//2 - sum(nums)
        