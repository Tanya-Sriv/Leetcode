class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        c = 0
        if n == 0:
            return False
        while n != 0:
            c +=1
            n &=(n-1)
            if c > 1:
                return False
        return True