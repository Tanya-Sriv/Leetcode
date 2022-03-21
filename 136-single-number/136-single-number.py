class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Method 2:
        c = Counter(nums)
        for i,v in c.items():
            if v < 2:
                return i
        # Method 1
        # nums.sort()
        # s = [nums[0]]
        # for i in range(1,len(nums)):
        #     if nums[i] != nums[i-1] :
        #         s.append(nums[i])
        #     else:
        #         s.remove(nums[i])
        # return s[0]
        
            
                
            
            
        