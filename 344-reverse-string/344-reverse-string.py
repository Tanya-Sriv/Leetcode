class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Method 1
        temp = ''
        for i in range(len(s)//2):
            temp = s[i]
            s[i] = s[-1*i -1]
            s[-1*i -1] = temp
        