class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l_id = 0
        r_id = len(nums)-1
        while l_id <= r_id:
            c_id = (l_id + r_id)//2
            
            if nums[c_id] == target:
                return c_id
            if nums[c_id] < target:
                l_id = c_id+1
            else:
                r_id = c_id-1
                
        return l_id
        