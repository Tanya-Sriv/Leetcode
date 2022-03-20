class Solution:
    def firstUniqChar(self, s: str) -> int:
        p = dict(Counter(s))
        for k in p.keys():
            if p[k] == 1:
                return s.index(k)
        return -1