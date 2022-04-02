class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        while n != 1:
            if n/2 != int(n/2):
                return False
            n = n/2
        return True 
        # c = 0
        # if n <= 0:
        #     return False
        # while n != 0:
        #     c +=1
        #     n &=(n-1)
        #     if c > 1:
        #         return False
        # return True
        