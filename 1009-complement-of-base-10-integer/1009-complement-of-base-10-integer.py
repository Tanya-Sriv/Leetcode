class Solution:
    def bitwiseComplement(self, n: int) -> int:
        # 101 111 => 010
        l = len(bin(n))-2
        return n^(2**l -1)