class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        digit = 0
        for i in nums:
            if len(str(i))%2 == 0:
                digit +=1
        return digit        