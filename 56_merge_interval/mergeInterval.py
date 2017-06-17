#Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

"""
Solution:
Sort the intervals by start time first.
Then iterate the sorted intervals, if intervals[i].start time is smaller than the last inteval in merged result which means they overlap, then update the end time of last entry in merged result (merge two intervals). Otherwise, they don't overlap, then simply add intervals[i] into merged result 

Time complexity: O(n), n is the size of intervals.
"""
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
    
        #sanity check
        if len(intervals) == 0:
            return []
        
        #sort the intervals by start time then end time
        intervals.sort(key=lambda x: (x.start, x.end))
        
        res = [intervals[0]]
        
        for intrv in intervals:
            if intrv.start <= res[-1].end:
                res[-1].end = intrv.end if intrv.end > res[-1].end else res[-1].end
            else:
                res.append(intrv)
        
        return res
                 

"""
test
"""
myTest = Solution()

#print myTest.merge([[1,3], [2,6], [8,10], [15,18]])
                    
