class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        res = []
        i = 0

        while i < len(intervals):
            j = i+1
            while j < len(intervals) and intervals[j][0]<= intervals[i][1]:
                intervals[i][1] = max(intervals[i][1], intervals[j][1])
                j+=1
            res.append([intervals[i][0], max(intervals[i][1], intervals[j-1][1])])
            i=j
        return res
            