class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        sq = [min(x) for x in rectangles]
        return sq.count(max(sq))
                
                    
                
        