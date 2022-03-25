class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        #Method 3: Runtime: 35 ms Memory:14 MB
        #using counter
        # s_c = Counter(s)
        # t_c = Counter(t)
        # for k in t_c.keys():
        #     if k not in s_c.keys() or t_c[k] != s_c[k]:
        #         return k
        
        # Method 4:
        t += s
        t_c = Counter(t)
        for k in t_c.keys():
            if t_c[k]%2 != 0:
                return k
        
        # Method1
        # if s == '':
        #     return t[0]
        # t=list(t)
        # for i in s:
        #     if i in t:
        #         t.pop(t.index(i))
        # return t[0]
        
        # Method 2:
        # s = list(s)
        # s.sort()
        # t = list(t)
        # t.sort()
        # for i in range(len(t)-1):
        #     if t[i] != s[i]:
        #         return t[i]
        # return t[-1]
        
        