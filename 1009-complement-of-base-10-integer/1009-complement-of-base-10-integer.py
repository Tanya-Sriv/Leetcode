class Solution:
    def bitwiseComplement(self, n: int) -> int:
        # 101 111 => 010
        n_binary = str(format(n,"b"))
        mask = int("1"*len(n_binary),2)
        return n^mask
        