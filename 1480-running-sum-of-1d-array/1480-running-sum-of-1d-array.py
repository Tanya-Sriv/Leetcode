class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        s = [nums[0]]
        for i in range(1, len(nums)):
            s.append(s[-1]+nums[i])
        return s