class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        # print(nums, len(nums))
        if len(nums)<3:
            return nums[0]
        for i in range(0,len(nums),3):
            if i <= len(nums)-3:
                print(nums[i],nums[i+1],nums[i+2])
                if nums[i] == nums[i+1] and nums[i+1] == nums[i+2]:
                    continue
                else:
                    return nums[i]
            else:
                return nums[-1]