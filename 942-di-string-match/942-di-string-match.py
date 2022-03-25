class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        mn, mx = 0,len(s)
        l = []
        for i in s:
            if i == 'I':
                l.append(mn)
                mn += 1
            elif i == 'D':
                l.append(mx)
                mx -= 1
        l.append(mx)
        return l