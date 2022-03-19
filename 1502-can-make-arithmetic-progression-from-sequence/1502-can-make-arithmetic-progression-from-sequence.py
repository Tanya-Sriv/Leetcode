class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = None
        prev_diff = None
        for i in range(1,len(arr)):
            diff = arr[i]-arr[i-1]
            if i == 1:
                prev_diff = diff
                continue
            else:
                if prev_diff != diff:
                    return False
                else:
                    prev_diff = diff
                    
        return True
            
            
        