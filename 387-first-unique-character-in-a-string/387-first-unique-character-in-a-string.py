class Solution:
    def firstUniqChar(self, s: str) -> int:
        p = dict(Counter(s))
        print(p)
        for k in p.keys():
            print(k, p[k])
            if p[k] == 1:
                return s.index(k)
        return -1