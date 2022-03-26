class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        # Method 1: Hamming weight [Runtime:34 ms Memory:13.8 MB]
        # while n != 0:
        #     n = n & (n-1)
        #     count +=1
        # return count
        
        #Method 2
        n = bin(n)
        for i in n:
            if i == '1':
                count+=1
        return count