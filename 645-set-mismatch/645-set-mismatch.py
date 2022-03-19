class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        mis, rep = None,None
        lookup = Counter(nums)
        for i in range(0, len(nums)+1):
            if i not in lookup:
                mis = i
            elif lookup[i] > 1:
                rep = i
        return [rep,mis]
            
