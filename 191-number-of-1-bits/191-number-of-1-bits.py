class Solution:
    def hammingWeight(self, n: int) -> int:
        # Method 1: Hamming weight [Runtime:34 ms Memory:13.8 MB]
        count = 0
        while n != 0:
            n &= n-1
            count +=1
        return count
        
        #Method 2
        # count = 0
        # n = bin(n)
        # for i in n:
        #     if i == '1':
        #         count+=1
        # return count