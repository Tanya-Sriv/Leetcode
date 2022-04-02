class Solution:
    # def fib(self, n: int) -> int:
        # Method 1:
        # fib = [0,1] 
        # if n <2:
        #     return n
        # for i in range(2,n+1):
        #     fib.append(fib[i-1]+fib[i-2])
        # return fib[-1]
        
        # Method 2: 
        # if n<2:
        #     return n
        # return self.fib(n-1)+self.fib(n-2)
        
    # Method 3: caching
    cache = {0:0,1:1}
    def fib(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]
        self.cache[n] = self.fib(n-1) + self.fib(n -2)
        return self.cache[n]