class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        count=len(intervals)
        covered=[False]*count
        for i in range(len(intervals)):
            for j in range(i+1,len(intervals)):
                if intervals[i][0]>=intervals[j][0] and intervals[i][1]<=intervals[j][1]:
                    covered[i]=True
                    break
                elif intervals[i][0]<=intervals[j][0] and intervals[i][1]>=intervals[j][1]:
                    covered[j]=True
        for i in covered:
            if i:
                count-=1
        return count

        