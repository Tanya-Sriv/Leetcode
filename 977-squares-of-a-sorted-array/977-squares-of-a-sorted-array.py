class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = []
        for i in nums:
             n.append(i*i)
        n.sort()
        return n