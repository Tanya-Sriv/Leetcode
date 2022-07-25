class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x:x[0])
        out = []           
        prev_start = intervals[0][0]
        prev_end = intervals[0][1]
        for i in range(1, len(intervals)):
            # if intervals[i][0] > prev_end:
            #     out.append([prev_start, prev_end])
            #     prev_start = intervals[i][0]
            #     prev_end = intervals[i][1]
            if intervals[i][0] >= prev_start and intervals[i][0] <= prev_end:
                prev_start = min(intervals[i][0], prev_start)
                prev_end = max(intervals[i][1],prev_end)
            elif intervals[i][0] <= prev_start:
                prev_start = min(intervals[i][0], prev_start)
                prev_end = max(intervals[i][1],prev_end)
            elif intervals[i][0] > prev_start or intervals[i][0] > prev_end:
                out.append([prev_start, prev_end])
                prev_start = intervals[i][0]
                prev_end = intervals[i][1]
        res = [prev_start, prev_end]
        out.append(res)    
        return out
        
                    
                    