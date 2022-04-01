class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occur = Counter(arr)
        n = []
        for val in occur.values():
            n.append(val)
        for val in Counter(n).values():
            if val > 1:
                return False
        return True