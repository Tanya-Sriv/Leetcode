class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # method 1: O(n2)
        # intervals = sorted(intervals, key=lambda x:x[0])
        # out = []           
        # prev_start = intervals[0][0]
        # prev_end = intervals[0][1]
        # for i in range(1, len(intervals)):
        #     if (intervals[i][0] >= prev_start and intervals[i][0] <= prev_end) or (intervals[i][0] <= prev_start):
        #         prev_start = min(intervals[i][0], prev_start)
        #         prev_end = max(intervals[i][1],prev_end)
        #     elif intervals[i][0] > prev_start or intervals[i][0] > prev_end:
        #         out.append([prev_start, prev_end])
        #         prev_start = intervals[i][0]
        #         prev_end = intervals[i][1]
        # out.append([prev_start, prev_end])    
        # return out
        
        # method 2: O(nlogn)/space:O(n)
        result = []
        intervals.sort(key = lambda x:x[0])
        for i in intervals:
            start, end = i
            if not result or result[-1][1] < start:
                result.append(i)
            else:
                result[-1][1] = max(result[-1][1], end)
        return result
        
        
                    
                    