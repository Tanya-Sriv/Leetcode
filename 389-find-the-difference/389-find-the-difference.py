class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # Method1
        if s == '':
            return t[0]
        t=list(t)
        for i in s:
            if i in t:
                t.pop(t.index(i))
        return t[0]
        # Method 2:
        # s = list(s)
        # s.sort()
        # t = list(t)
        # t.sort()
        # for i in t:
        #     if i not in s:
        #         return i