class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        mx, mn = len(s),0
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