class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        l = len(nums)
        if l<3:
            return nums[0]
        for i in range(0,l-2,3):
            if i <= l-3:
                if nums[i] == nums[i+1] and nums[i+1] == nums[i+2]:
                    continue
                else:
                    return nums[i]
        return nums[-1]