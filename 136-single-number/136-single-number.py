class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Method 1
        for i,v in Counter(nums).items():
            if v < 2:
                return i
        # Method 2
        # nums.sort()
        # s = [nums[0]]
        # for i in range(1,len(nums)):
        #     if nums[i] != nums[i-1] :
        #         s.append(nums[i])
        #     else:
        #         s.remove(nums[i])
        # return s[0]
        
            
                
            
            
        