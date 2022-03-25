class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        mx = len(s)
        mn = 0
        l = []
        for i in s:
            if i == 'D':
                l.append(mx)
                mx -= 1
            elif i == 'I':
                l.append(mn)
                mn += 1
        l.append(mx)
        return l