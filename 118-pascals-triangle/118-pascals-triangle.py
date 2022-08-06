class Solution:
    def generate(self, n: int) -> List[List[int]]:
        pas = [[1]]
        temp = []
        for i in range(1, n):
            # temp = [1]
            prev_row = pas[-1]
            for j in range(len(prev_row)+1):
                if j == 0 or j == len(prev_row):
                    s = 1
                else:
                    s = prev_row[j-1] + prev_row[j]
                temp.append(s)
            pas.append(temp)
            temp = []
        return pas