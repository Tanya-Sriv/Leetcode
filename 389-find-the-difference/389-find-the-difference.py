class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # Method1
        # if s == '':
        #     return t[0]
        # t=list(t)
        # for i in s:
        #     if i in t:
        #         t.pop(t.index(i))
        # return t[0]
        # Method 2:
        s = list(s)
        s.sort()
        t = list(t)
        t.sort()
        for i in range(len(t)-1):
            if t[i] != s[i]:
                return t[i]
        return t[-1]