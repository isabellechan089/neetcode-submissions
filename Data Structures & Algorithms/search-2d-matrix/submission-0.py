class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        combined = []
        for l in matrix:
            combined+= l
        
        def search(left, right):
            if left>right:
                return False
            
            middle = (left+right) //2
            if combined[middle] == target:
                return True
            elif combined[middle] > target:
                return search(left, middle-1)
            else: return search(middle+1, right)
        return search(0, len(combined)-1)