class Solution:
    def hammingWeight(self, n: int) -> int:
        # Method 1: Hamming weight [Runtime:34 ms Memory:13.8 MB]
        count = 0
        while n != 0:
            n = n & (n-1)
            count +=1
        return count
        
        #Method 2 [Runtime:35 ms Memory:13.8 MB]
        # count = 0
        # n = bin(n)
        # for i in n:
        #     if i == '1':
        #         count+=1
        # return count
        
        # Method 3: using mask 
        # count = 0
        # while n !=0:
        #     if n & 1 == 1:
        #         count+=1
        #     n >> 1
        
        
        
        