class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Method 1
        s = []
        for i in nums:
            if i not in s:
                s.append(i)
            else:
                s.remove(i)
        return s[0]
            
            
        