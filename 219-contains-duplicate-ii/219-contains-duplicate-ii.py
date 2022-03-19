class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == len(set(nums)):
            return False
        if len(nums) <= k + 1:  
            return True

        for i in range(len(nums) - k):
            if len(nums[i:(i + k + 1)]) != len(set(nums[i:(i + k + 1)])):
                return True

        return False