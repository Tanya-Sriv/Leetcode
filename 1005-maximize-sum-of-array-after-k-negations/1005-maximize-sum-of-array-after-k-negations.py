class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        while k > 0:
            nums.sort()
            if min(nums) == 0:
                return sum(nums)
            nums[0]*=(-1)
            k -=1
        return sum(nums)