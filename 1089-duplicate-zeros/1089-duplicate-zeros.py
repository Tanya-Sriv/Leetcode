class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        myiter = iter(range(0, len(arr)-1))
        for i in myiter:
            if arr[i] == 0:
                j = len(arr)- 2
                for j in range(len(arr)-2, i,-1):
                    arr[j+1] = arr[j]
                arr[i+1] = 0
                next(myiter,None)