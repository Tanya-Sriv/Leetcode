class Solution:
    def isValid(self, s: str) -> bool:
        d = {')':'(','}':'{', ']':'['}
        l =len(s)
        arr = []
        if l <2:
            return False
        for k in range(l):
            if len(arr)>0: 
                if s[k] in d and arr[-1]==d[s[k]]:
                    # print(s[k])
                    arr.pop(-1)
                else:
                    arr.append(s[k])
            else:
                arr.append(s[k])
        #     print(arr)
        # print("---")
        return True if arr==[] else False