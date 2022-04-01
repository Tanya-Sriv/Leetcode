class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ''
        l1 = len(word1)
        l2 = len(word2)
        i = 0
        j = 0
        while i < l1 or j < l2:
            if i >= l1 and j < l2:
                ans += word2[j:l2]
                return ans
            elif i < l1 and j >= l2:
                ans += word1[i:l1]
                return ans
            elif i < l1 and j < l2:
                if i < l1:
                    ans += word1[i]
                    i+=1
                if j < l2:
                    ans += word2[j]
                    j+=1
        return ans
        
        
        