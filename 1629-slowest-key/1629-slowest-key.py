class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        max_duration = [releaseTimes[0], keysPressed[0]]
        for i in range(1,len(releaseTimes)):
            dur = releaseTimes[i] - releaseTimes[i-1]
            if dur > max_duration[0]:
                max_duration = [dur, keysPressed[i]]
            elif dur == max_duration[0]:
                max_duration = [dur, max(max_duration[1],keysPressed[i])]
        return max_duration[1]
        