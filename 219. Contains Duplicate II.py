# 219. Contains Duplicate II
# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such
# that nums[i] == nums[j] and abs(i - j) <= k.

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        if len(nums) == len(set(nums)):
            return False
        if len(nums) <= k + 1:
            return True

        for i in range(len(nums) - k):
            if len(nums[i:(i + k + 1)]) != len(set(nums[i:(i + k + 1)])):
                return True

        return False