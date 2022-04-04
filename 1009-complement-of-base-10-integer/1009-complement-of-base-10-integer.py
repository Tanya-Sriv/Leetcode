class Solution:
    def bitwiseComplement(self, n: int) -> int:
        # 101 111 => 010
        # Method 2:
        n_binary = str(format(n,"b"))
        mask = int("1"*len(n_binary),2)
        return n^mask
        # Method 1: Runtime: 30 ms	Memory:13.8 MB
        # l = len(bin(n))-2
        # mask = 2**l -1
        # return n^mask