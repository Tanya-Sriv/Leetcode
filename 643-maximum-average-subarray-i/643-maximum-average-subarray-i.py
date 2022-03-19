class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = [nums[0]]
        i = 0
        for i in range(1,len(nums)):
            s.append(s[i-1]+ nums[i])
        sm,i = s[k-1]/k ,k
        while i<len(nums):
            sm = max(sm, (s[i]-s[i-k])/k)
            i+=1     
        return sm