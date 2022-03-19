class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #array sort
        #iter through element- if element present -> dic[val] = not null return true else skip.
        nums.sort()
        log = {}
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
            else:
                continue
        return False
        
        
        