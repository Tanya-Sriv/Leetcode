class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Method 1:
        # temp = ''
        # for i in range(len(s)//2):
        #     temp = s[i]
        #     s[i] = s[-1*i -1]
        #     s[-1*i -1] = temp
        d = {index: value for index, value in enumerate(s)}
        l = len(s)
        for i in range(l//2):
            s[i] = d[l-i-1]
            s[-1*i -1] = d[i]