class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        lucky = []
        m = len(matrix) #row
        n = len(matrix[0]) #column
        c, r = 0,0
        for row in matrix:
            c = row.index(min(row))
            temp =[]
            for rw in matrix:
                temp.append(rw[c])
            r = temp.index(max(temp))
            if row[c] == matrix[r][c]:
                lucky.append(row[c])
         
        return lucky
            