class Solution:
    def isValid(self, s: str) -> bool:
        d = {')':'(','}':'{', ']':'['}
        arr = []
        if len(s) <2:
            return False
        for k in range(len(s)):
            if arr: 
                # to check if closing bracket and if openning bracket already used                                   
                arr.pop(-1) if s[k] in d and arr[-1]==d[s[k]] else arr.append(s[k]) 
            else:
                # if openning bracket and if previous pairs found already and ths one is new combination                                  
                arr.append(s[k])
        return True if arr==[] else False