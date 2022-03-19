class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # nums = self.nums
        new_list= []
        for idx, val in enumerate(nums):
            if(idx == 0):
                new_list.append(val)
            elif (idx > 0):
                if(val != prev):
                    new_list.append(val)
            else:
                pass     
            prev = val
            
        for idx in range(0, len(nums)):
            if(idx<len(new_list)):
                nums[idx] = new_list[idx]
            else:
                nums[idx] = '_'
        
            
        return len(new_list)