class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if s == '':
            if len(t) == 1:
                return t[0]
            else:
                return t
        t=list(t)
        for i in s:
            if i in t:
                t.pop(t.index(i))
        return t[0]