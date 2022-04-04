class Solution:
    def bitwiseComplement(self, n: int) -> int:
        # 101 111 => 010
        l = len(bin(n))-2
        mask = 2**l -1
        return n^mask